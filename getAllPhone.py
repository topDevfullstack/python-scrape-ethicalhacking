from twilio.rest import Client
import os

# Your Twilio credentials
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

# Create a Twilio client
client = Client(account_sid, auth_token)

def retrieve_sms():
    # Retrieve messages sent to your Twilio number
    messages = client.messages.list()

    for message in messages:
        print(f"From: {message.from_}, To: {message.to}, Body: {message.body}, Date: {message.date_sent}")

if __name__ == "__main__":
    retrieve_sms()