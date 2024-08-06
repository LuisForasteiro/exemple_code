from src.utils.email_utils import send_email

def send_notification(subject, message, recipients):
    send_email(subject, message, recipients)
