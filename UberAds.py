import os
from twilio.rest import Client

n = 0
imageFilePath = '/images/'


def send_mms(n):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Welcome to UberAds',
        media_url=imageFilePath + 'image' + str(n) + '.png',
        from_='YOUR TWILIO NUMBER',
        to='PHONE NUMBER'
    )


if __name__ == '__main__':
    for n in range(1, 16):
        send_mms(n)




