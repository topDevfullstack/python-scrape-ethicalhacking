import os
import random
from twilio.rest import Client

# Twilio credentials from environment variables
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_number = os.environ.get('TWILIO_PHONE_NUMBER')

# Create a Twilio client
client = Client(account_sid, auth_token)

# List of users and their phone numbers
users = [
    {"name": "Alice", "phone": "+1234567890"},
    {"name": "Bob", "phone": "+0987654321"},
    # Add more users as needed
]

def generate_verification_code():
    """Generate a 4-digit random verification code."""
    return random.randint(1000, 9999)

def send_sms(to, code):
    """Send an SMS code to the specified phone number."""
    try:
        message = client.messages.create(
            body=f"Your verification code is: {code}",
            from_=twilio_number,
            to=to
        )
        print(f"Message sent to {to}: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {to}. Error: {e}")

# Example usage to send SMS codes to all users
if __name__ == "__main__":
    for user in users:
        code = generate_verification_code()
        send_sms(user["phone"], code)