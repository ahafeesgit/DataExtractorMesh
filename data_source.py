
import sqlite3
from file_manipulator import FileManipulator
from database import Database
import requests
import json
import pandas as pd
import datetime;
from behaviour_manipulator import BehaviourManipulator
from email_sender import EmailSender
import grpc
from picker_pb2_grpc import PickerControllerServiceStub
from picker_pb2 import  GetActivePickerRequest
from loyalty import Loyalty

class DataSource:

    ORDER_STATUS = 'PICKED_UP,DISPATCHED,PICKED_UP_BY_CUSTOMER,CANCELLED,HANDLED_EXTERNALLY'
    ORDER_SORT = 'lastShopperInteractionTime,desc'
    ORDER_SIZE = 20
    ORDER_BASE_URL = 'https://me-shopper-api.shopper.deliveryhero.net/pelican/v1/orders'
    ORDER_HOST='me-shopper-api.shopper.deliveryhero.net'

    AUTH_BASE_URL = 'https://picker-asia.dh-auth.io/api/v5/oauth2/token'
    AUTH_HOST='picker-asia.dh-auth.io'
    CLIENT_ID = 'pelican'
    CLIENT_SECRET = 'aoJmlkUHyY44Un35eJ98t71UQ6CGNwmSER2K'
    AUTH_GRAND_TYPE = 'password'
    AUTH_SCOPE = 'keymaker.picker.user.pelican.password'

    USER_AGENT = 'okhttp/4.9.3'
    LANGUAGE='en'
    APP_VERSION = "2.30.2"
    APP_VERSION_CODE = "69"

    GLOBAL_ENTITY_ID = "TB_KW"

    def loginUser(user_name,password):
        BehaviourManipulator.fake_human_behaviour(True)
        header_data = {"Content-Type":"application/json","Connection":"Keep-Alive","User-Agent":DataSource.USER_AGENT,"host":DataSource.AUTH_HOST,"x-global-entity-id":DataSource.GLOBAL_ENTITY_ID}
        url = DataSource.AUTH_BASE_URL
        data = {"client_id": DataSource.CLIENT_ID, "client_secret": DataSource.CLIENT_SECRET, "grant_type": DataSource.AUTH_GRAND_TYPE, "password": str(password), "scope": DataSource.AUTH_SCOPE, "username": user_name}
        response = requests.post(url, data=json.dumps(data), headers=header_data)
        if(response.status_code == 200):
            return True,response.json()["access_token"], response.json()["refresh_token"], response.json()["expires_in"]
        else:
            return False,'','',''

    def getActivePicker(pelican_token,store_id,refresh_token,expires_in):
            channel = grpc.secure_channel('picker-mgmt-grpc-me-live.deliveryhero.io',grpc.ssl_channel_credentials(),options=(('grpc.enable_http_proxy', 0),))
            client = PickerControllerServiceStub(channel)
            request = GetActivePickerRequest()
            auth_bearer_token = 'Bearer ' + 'ffefe233-5989-478d-805b-843a14a489cf'
            auth_pelican_token = 'Bearer ' + pelican_token
            metadata = (('pelicantoken', auth_pelican_token),('authorization',auth_bearer_token))
            response = client.GetActivePicker(request=request, metadata=metadata)
            DataSource.updateStoreToken(store_id,response.picker_jwt_token,refresh_token,expires_in)
            return response.picker_jwt_token,response.profile.first_name
            
    def getOrderList(token,vendor,vendor_name,device_id,page,clientId):
        BehaviourManipulator.fake_human_behaviour(False)
        url = DataSource.ORDER_BASE_URL +'?'+'vendors='+str(vendor).rstrip(".0") +'&status='+DataSource.ORDER_STATUS+'&size='+str(DataSource.ORDER_SIZE)+'&page='+str(page)+'&sort='+DataSource.ORDER_SORT
        header_data = {"Authorization": "Bearer "+token,"x-app-version":DataSource.APP_VERSION,"x-app-version-code":DataSource.APP_VERSION_CODE,"x-device-id":device_id,"x-locale":DataSource.LANGUAGE,"User-Agent":DataSource.USER_AGENT,"host":DataSource.ORDER_HOST}
        response = requests.get(url,headers=header_data)
        if(response.status_code == 200):
            order_array = response.json()["orders"]
            orders_data = []
            for order in order_array:
                order_data = [order['id'],order['externalId'],order['vendorId'],order['vendorDisplayName'],order['firstName'],order['lastName'],order['phone'],order['productCount'],order['total'],order['paymentTypeDetails'],order['pickupTime']]
                orders_data.append(order_data)
                DataSource.saveCustomerDetails(order['id'],order['externalId'],order['productCount'],order['feesTotal'],order['total'],order['paymentTypeDetails'],order['pickupTime'],order['firstName'],order['lastName'],order['phone'],vendor,token,device_id,clientId)
            df = pd.DataFrame(orders_data,columns=['id','externalId','vendorId', 'vendorDisplayName', 'firstName','lastName','phone','productCount','total','paymentTypeDetails','pickupTime'])
            #df.to_excel('data/output/'+vendor_name+str(datetime.datetime.now())+'.xlsx', index=False, header=True)
            total_page = response.json()["pagination"]["totalPages"]
            if(page+1 < total_page):
                DataSource.getOrderList(token,vendor,vendor_name,device_id,page+1,clientId)
            else:
                return
        else:
            #print(response)
            return

        
    def getOrderDetails(reference_id,order_id,token,device_id):
        BehaviourManipulator.fake_human_behaviour(False)
        url = DataSource.ORDER_BASE_URL +'/'+reference_id
        header_data = {"Authorization": "Bearer "+token,"x-app-version":DataSource.APP_VERSION,"x-app-version-code":DataSource.APP_VERSION_CODE,"x-device-id":device_id,"x-locale":DataSource.LANGUAGE,"User-Agent":DataSource.USER_AGENT,"host":DataSource.ORDER_HOST}
        response = requests.get(url,headers=header_data)
        if(response.status_code == 200):
            products_array = response.json()["order"]["products"]
            for product in products_array:
                 display_barcode = ''
                 if product['barcodes'] is None:
                    display_barcode = ''
                 else:
                    display_barcode = ','.join(product['barcodes'])
                 DataSource.saveOrderProduct(product['sku'],display_barcode,product['name'],product['price'],order_id)
            return
        else:
            #print(response)
            return

    def getStoreList(clientId):
         database,cursor = Database.getDatabaseConnection()
         try:
            #print("Connected to SQLite")
            sqlite_select_query = """SELECT 
            StoresTbl.id,
            StoresTbl.store_id,
            StoresTbl.user_name,
            StoresTbl.password,
            StoresTbl.token,
            StoresTbl.refresh_token,
            StoresTbl.expires_in,
            StoresTbl.device_id,
            StoresTbl.store_name
            FROM StoresTbl WHERE StoresTbl.client_id = '"""+str(clientId)+"""';"""

            branches = cursor.execute(sqlite_select_query).fetchall()
            return branches
         except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
            return 
         finally:
            if database:
                database.close()
                #print("The SQLite connection is closed")

    def updateStoreToken(id,token,refresh_token,expires_in):
         database,cursor = Database.getDatabaseConnection()
         try:
            #print("Connected to SQLite")
            sqlite_update_query = "UPDATE StoresTbl SET token = '"+token+"',refresh_token = '"+refresh_token+"',expires_in = '"+str(expires_in)+"',device_id = '"+str(BehaviourManipulator.generate_fake_device_id())+"' WHERE id = '"+str(id)+"' ;"
            #print(sqlite_update_query)
            cursor.execute(sqlite_update_query)
            database.commit()
         except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
            return 
         finally:
            if database:
                database.close()
                #print("The SQLite connection is closed")

    def saveCustomerDetails(ref_id,external_id,product_count,delivery_fee,total_amount,payment_type_details,pickup_time,first_name,last_name,phone_number,store_id,token,device_id,client_id):
         if(DataSource.checkIfOrderExist(ref_id) == True):
            return
         print('saving customer '+str(first_name))
         database,cursor = Database.getDatabaseConnection()
         try:
            #print("Connected to SQLite")
            sqlite_select_query = """SELECT CustomersTbl.id,
            CustomersTbl.product_count,
            CustomersTbl.total_amount,
            CustomersTbl.total_order,
            CustomersTbl.client_id
            FROM CustomersTbl WHERE CustomersTbl.phone_number = '"""+phone_number+"""' AND CustomersTbl.client_id = '"""+str(client_id)+"""';"""
            #print (sqlite_select_query)
            customer = cursor.execute(sqlite_select_query).fetchone()

            customer_id = -1
            #print(customer)
            if customer is not None:
                customer_id = customer[0]
                new_product_count = customer[1]+product_count
                new_total_amount = customer[2]+total_amount
                new_total_orders = customer[3]+1
                sqlite_update_query = "UPDATE CustomersTbl SET product_count = '"+str(new_product_count)+"',total_amount = '"+str(new_total_amount)+"',total_order = '"+str(new_total_orders)+"' WHERE phone_number = '"+phone_number+"' AND client_id = '"+str(client_id)+"';"
                #print(sqlite_update_query)
                cursor.execute(sqlite_update_query)
                database.commit()

            else:
                #sqlite_insert_query = "INSERT INTO CustomersTbl (first_name,last_name,phone_number,product_count,total_amount,total_order,client_id) VALUES ('"+first_name+"','"+last_name+"','"+phone_number+"','"+str(product_count)+"','"+str(total_amount)+"','1','"+str(client_id)+"');"
                sqlite_insert_query = "INSERT INTO CustomersTbl (first_name,last_name,phone_number,product_count,total_amount,total_order,client_id) VALUES (?,?,?,?,?,?,?)"
                cursor.execute(sqlite_insert_query,(first_name,last_name,phone_number,str(product_count),str(total_amount),'1',str(client_id)))
                database.commit()

                sqlite_last_inserted_id = "SELECT id from CustomersTbl order by id DESC limit 1;"
                last_inserted_id = cursor.execute(sqlite_last_inserted_id)
                customer_id = last_inserted_id.fetchone()[0]
                database.commit()
            order_id = DataSource.saveOrderData(ref_id,external_id,product_count,delivery_fee,total_amount,payment_type_details,pickup_time,customer_id,store_id)
            DataSource.getOrderDetails(ref_id,order_id,token,device_id)
         except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
            return
         finally:
            if database:
                database.close()
                #print("The SQLite connection is closed")

    def syncLoyaltyInfo(customer_id,loyalty_id):
         database,cursor = Database.getDatabaseConnection()
         try:
            sqlite_update_query = "UPDATE CustomersTbl SET loyalty_id = '"+str(loyalty_id)+"' WHERE id = '"+customer_id+"';"
            #print(sqlite_update_query)
            cursor.execute(sqlite_update_query)
            database.commit()
         except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
            return
         finally:
            if database:
                database.close()

    def saveOrderData(ref_id,external_id,product_count,delivery_fee,total_amount,payment_type_details,pickup_time,customer_id,store_id):

        print('saving order '+str(ref_id) + ' of customer '+str(customer_id))
        total_without_delivery = total_amount - delivery_fee
        database,cursor = Database.getDatabaseConnection()
        try:
            #sqlite_insert_query = "INSERT INTO OrdersTbl (reference_id,external_id,product_count,payment_type_details,pickup_time,total_amount,customer_id,store_id,deliver_charge,amount) VALUES ('"+ref_id+"','"+external_id+"','"+str(product_count)+"','"+payment_type_details+"','"+pickup_time+"','"+str(total_amount)+"','"+str(customer_id)+"','"+str(store_id)+"','"+str(delivery_fee)+"','"+str(total_without_delivery)+"');"
            sqlite_insert_query = "INSERT INTO OrdersTbl (reference_id,external_id,product_count,payment_type_details,pickup_time,total_amount,customer_id,store_id,deliver_charge,amount) VALUES(?,?,?,?,?,?,?,?,?,?)"

            #print(sqlite_insert_query)
            cursor.execute(sqlite_insert_query,(ref_id,external_id,str(product_count),payment_type_details,pickup_time,str(total_amount),str(customer_id),str(store_id),str(delivery_fee),str(total_without_delivery)))
            database.commit()

            sqlite_last_inserted_id = "SELECT id from OrdersTbl order by id DESC limit 1;"
            last_inserted_id = cursor.execute(sqlite_last_inserted_id)
            order_id = last_inserted_id.fetchone()[0]
            database.commit()
            return order_id
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
            return ''
        finally:
            if database:
                database.close()
                #print("The SQLite connection is closed")
    def saveOrderProduct(sku,barcodes,product_name,product_price,order_id):

        print('saving products('+product_name+') of order'+str(order_id))
        database,cursor = Database.getDatabaseConnection()

        try:
            #sqlite_insert_query = "INSERT INTO OrderItemsTbl (sku,barcodes,name,tota_price,order_id) VALUES(?,?,?,?,?) ('"+str(sku)+"','"+barcodes+"','"+product_name+"','"+str(product_price)+"','"+str(order_id)+"');"
            sqlite_insert_query = "INSERT INTO OrderItemsTbl (sku,barcodes,name,tota_price,order_id) VALUES(?,?,?,?,?)"

            #print(sqlite_insert_query)
            cursor.execute(sqlite_insert_query,(str(sku),barcodes,product_name,str(product_price),str(order_id)))
            database.commit()
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
            return
        finally:
            if database:
                database.close()
                #print("The SQLite connection is closed")

    def checkIfOrderExist(ref_id):
         database,cursor = Database.getDatabaseConnection()
         is_exist = False
         try:
            #print("Connected to SQLite")
            sqlite_select_query = """SELECT OrdersTbl.id FROM OrdersTbl WHERE OrdersTbl.reference_id = '"""+ref_id+"""';"""

            #print(sqlite_select_query)
            orders = cursor.execute(sqlite_select_query).fetchone()
            #print(sqlite_select_query)
            #print(orders)
            if orders is not None:
               is_exist = True
            else:
               is_exist = False


         except sqlite3.Error as error:
             print("Failed to read data from sqlite table", error)
             return
         finally:
            if database:
                 database.close()
                 #print("The SQLite connection is closed")
         return is_exist

    def getCustomerList(clientId):
        database,cursor = Database.getDatabaseConnection()
        try:
           #print("Connected to SQLite")
           sqlite_select_query = "SELECT first_name, last_name, phone_number, product_count, total_amount, total_order FROM CustomersTbl WHERE client_id  = '"+str(clientId)+"';"

           customers = cursor.execute(sqlite_select_query).fetchall()
           return customers
        except sqlite3.Error as error:
           print("Failed to read data from sqlite table", error)
           return
        finally:
           if database:
               database.close()
               #print("The SQLite connection is closed")
    def getClientList():
        database,cursor = Database.getDatabaseConnection()
        try:
           sqlite_select_query = """SELECT id FROM ClientTbl;"""

           clients = cursor.execute(sqlite_select_query).fetchall()
           return clients
        except sqlite3.Error as error:
           print("Failed to read data from sqlite table", error)
           return
        finally:
           if database:
               database.close()

    def getEmailUserList(clientId):
        database,cursor = Database.getDatabaseConnection()
        try:
           #print("Connected to SQLite")
           sqlite_select_query = "SELECT email, name FROM MailUserTbl WHERE client_id  = '"+str(clientId)+"';"

           users = cursor.execute(sqlite_select_query).fetchall()
           return users
        except sqlite3.Error as error:
           print("Failed to read data from sqlite table", error)
           return
        finally:
           if database:
               database.close()

    def exportData(clientId):

        customers = DataSource.getCustomerList(clientId)
        customers_data = []
        for row in customers:
            customer_data = [row[0],row[1],row[2]]
            customers_data.append(customer_data)
        df = pd.DataFrame(customers_data,columns=['First Name','Last Name','Phone'])
        filePath = 'data/output/customer/'+str(datetime.datetime.now())+'.xlsx'
        df.to_excel(filePath, index=False, header=True)
        users = DataSource.getEmailUserList(clientId)
        for row in users:
            info = EmailSender.sendEmail(email = row[0],name = row[1],subject = 'Customer List',message = 'Please find the attached customer list',file_url = filePath)
            print(info)

    def syncToLoyalty(phone,email,first_name,last_name,customer_id):
        loyalty_id = Loyalty.sendData(phone,email,first_name,last_name)
        DataSource.syncLoyaltyInfo(customer_id,loyalty_id)



