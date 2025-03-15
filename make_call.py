from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
TO_NUMBER = os.getenv('TO_NUMBER')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

call = client.calls.create(
    twiml='<Response><Say voice="alice">Hello! This is a test call from Twilio.</Say></Response>',
    from_=TWILIO_NUMBER,
    to=TO_NUMBER
)

print(f"Call initiated! SID: {call.sid}")

"""
Using Twilio
Register for a free Twilio account and get a free phone number. You will also need to install the Twilio Python library using pip install twilio.
After signing up, you get $15 credits
Copy your ACCOUNT_SID, AUTH_TOKEN and TWILIO_NUMBER from your dashboard
Lastly make sure your personal number (TO_NUMBER) is among the verified numbers, if not add it

This is for testing purposes.
"""
