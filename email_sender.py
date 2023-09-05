
import random
import time
import requests

class EmailSender:
    MAILGUN_URL = 'https://api.eu.mailgun.net/v3/mg.easy-update.app/messages'
    MAILGUN_KEY = 'fdab7434d080580865587063c86335fe-4c2b2223-32998288'

    def sendEmail(email,name,subject,message,file_url):

            f = open(file_url, 'rb')
            r = requests.post(
                EmailSender.MAILGUN_URL,
                auth=("api", EmailSender.MAILGUN_KEY),
                data={
                    "subject": subject,
                    "from": "mail@mg.easy-update.app",
                    "to": email,
                    "text": message,
                    "html": "The<br>html"
                },
                files=[("attachment", f)],
            )
            f.close()
            return r.text





