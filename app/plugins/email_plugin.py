import smtplib
from email.mime.text import MIMEText

from semantic_kernel.functions.kernel_function_decorator import kernel_function
from email_service.email_sender import EmailSender

class EmailPlugin:
    def __init__(self, email_sender:EmailSender):
        self.email_sender=email_sender

    @kernel_function(name="send_email", description="Sends an email to a recipient with a subject and body")
    def send_email(self, to: str, subject: str, body: str) -> str:
        self.email_sender.send_email(
            to,
            subject,
            body
        )

        return f"Email enviado a {to} con asunto '{subject}'"
