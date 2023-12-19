import requests
import json

#Config
webhook_url = "" # Discord Webhook URL
webhook_message = "" # Message that will be sent to the webhook

#Webhook funtion
def send_webhook_message(content):
    data = {
        "content": content
    }
    response = requests.post(
        webhook_url, data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 204:
        raise ValueError(
           'Request to webhook returned an error %s, the response is:\n%s'
           % (response.status_code, response.text)
        )

send_webhook_message(webhook_message)