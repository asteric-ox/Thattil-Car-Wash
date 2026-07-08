import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load env from backend folder
load_dotenv('backend/.env')

def test_email():
    sender_email = "thattilservicecentree@gmail.com"
    sender_password = "yxtyobeyrlluthyg"
    to_email = "delvindavis031@gmail.com" # Test recipient
    
    print(f"Testing with: {sender_email}")
    
    msg = MIMEMultipart()
    msg['From'] = f"D2 TEST <{sender_email}>"
    msg['To'] = to_email
    msg['Subject'] = "Flask Email Test"
    msg.attach(MIMEText("This is a test from the Flask server.", 'plain'))

    try:
        print("Connecting to SMTP (SSL)...")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.set_debuglevel(1)
        print("Logging in...")
        server.login(sender_email, sender_password)
        print("Sending...")
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_email()
