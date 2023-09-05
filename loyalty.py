
import random
import time
import requests
import json
import phonenumbers

class Loyalty:

    GAMEBALL_BASE_URL = "https://api.gameball.co/api/v3.0/integrations"
    GAMEBALL_API_KEY = "5df29cb0f61a4f24ae55c5c4c77cfd5d"
    def sendData(phone,email,first_name,last_name):
        phone = Loyalty.trimCountryCode(phone)
        print(phone)
        url = Loyalty.GAMEBALL_BASE_URL + "/player"

        playerAttributes = {"displayName":first_name,
                            "firstName":first_name,
                            "lastName":last_name,
                            "mobile":phone,
                            "email":"",
                            "tags":"talabat"}
        data = {"playerUniqueId": phone,
                "mobile": phone,
                "email": email,
                "playerAttributes": playerAttributes,
                "referrerCode": "",
                "levelOrder": "",
                "deviceToken": ""}


        headers = {"APIKey":Loyalty.GAMEBALL_API_KEY,'Content-type': 'application/json'}
        #print(data)
        response = requests.post(url, data=json.dumps(data), headers=headers)

        return json.loads(response.content)["gameballId"]

    def trimCountryCode(phone):
        try:
            mobileNo=phonenumbers.parse(phone)
            return mobileNo.national_number
        except Exception as e:
            print("error in phone number "+str(e))
            return phone





