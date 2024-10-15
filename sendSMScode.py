from twilio.rest import Client
import random

# Your Account SID and Auth Token from twilio.com/console
account_sid = "your_account_sid"  # Replace with your Account SID
auth_token = "your_auth_token"  # Replace with your Auth Token

# Create a client instance
client = Client(account_sid, auth_token)


def generate_verification_code():
    """Generate a 4-digit random verification code."""
    return random.randint(1000, 9999)


def send_sms(to, body):
    message = client.messages.create(
        to=to,  # Recipient's phone number
        from_="your_twilio_phone_number",  # Your Twilio phone number
        body=body,
    )
    return message.sid


# Example usage
recipient_phone_number = "+380632311376"  # Replace with recipient's phone number
sms_body = generate_verification_code()
message_sid = send_sms(recipient_phone_number, sms_body)

print(f"Message sent with SID: {message_sid}")
