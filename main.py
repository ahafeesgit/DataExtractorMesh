import logging
from file_manipulator import FileManipulator
from data_source import DataSource
import schedule
import time

from behaviour_manipulator import BehaviourManipulator
import pandas as pd
import time
import schedule
import time
from email_sender import EmailSender
from loyalty import Loyalty

def extractData():
    logging.debug("Starting")
    print('Starting')
    clients = DataSource.getClientList()
    loopClientList(clients)
    print('Finished')
    logging.debug("Finished")

def loopClientList(clientList):
    for row in clientList:
        print(row[0])
        loopStoreList(row[0])
    print('All Clients Completed')




def loopStoreList(clientId):
    stores = DataSource.getStoreList(clientId)
    for row in stores:
        if not(row[2] is None) and not(row[3] is None):
            if (row[4] is None or row[4] == ''):
                login_status,pelican_token,refresh_token,expires_in = DataSource.loginUser(row[2],row[3])
                if login_status:
                    #get order list
                    #print(pelican_token)
                    jwt_token, store_name = DataSource.getActivePicker(pelican_token,row[0],refresh_token,expires_in)
                    DataSource.getOrderList(jwt_token,row[1],row[8],row[7],0,clientId)
            else:
                #check token expiry
                #print('check token expiry')
                if time.time() > row[6]:
                    print('Login')
                    login_status,pelican_token,refresh_token,expires_in = DataSource.loginUser(row[2],row[3])
                    if login_status:
                        #get order list
                        #print(pelican_token)
                        jwt_token, store_name = DataSource.getActivePicker(pelican_token,row[0],refresh_token,expires_in)
                        DataSource.getOrderList(jwt_token,row[1],row[8],row[7],0,clientId)
                else:
                    #get order list
                    print('Getting order list')
                    DataSource.getOrderList(row[4],row[1],row[8],row[7],0,clientId)

        else:
            print('No Data Available')

    print('Exporting data of: '+str(clientId))
    DataSource.exportData(clientId)
    print('Task Completed: '+str(clientId))

#extractData()
logging.basicConfig(filename="log.txt", level=logging.DEBUG,format="%(asctime)s %(message)s", filemode="w")

#schedule.every(15).minutes.do(extractData)
schedule.every(1).hour.do(extractData)
#schedule.every().day.at("10:30").do(job)

while(True):
    schedule.run_pending()
    time.sleep(1)

