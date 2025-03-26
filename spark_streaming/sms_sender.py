from twilio.rest import Client

def send_sms(message, to_phone_number):
    # Your Twilio account SID and Auth token
    account_sid = 'AC012c3f42a4c192bff513444258dd9654'  # Your Account SID
    auth_token = '778c81b1b32e52ed4a8f1d3ad07d2187'    # Your Auth Token
    
    # Your Twilio phone number (you can find this in your Twilio dashboard)
    from_phone_number = '+17853478267'  # Replace with your Twilio number
    
    # Create a Twilio client
    client = Client(account_sid, auth_token)
    
    # Send the SMS
    message = client.messages.create(
        body=message,
        from_=from_phone_number,
        to=to_phone_number
    )
    
    print(f"Message sent! SID: {message.sid}")

# Example usage
send_sms("Suspicious transaction detected! Amount: $5000, Location: Tokyo", "+212663248717")
