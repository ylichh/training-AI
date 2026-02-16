import os
import smtplib
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password

    def send_email(self, to: str, subject: str, body: str) -> str:
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = self.user
            msg["To"] = to

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.user, self.password)
                server.send_message(msg)

            return f"Email enviado a {to} con asunto '{subject}'"

if __name__=="__main__":
    email_sender=EmailSender(
          user="vbp.2112@gmail.com",
          password="axvhteasjlbuvrzm",
    )
    email_sender.send_email(
         to="vladimirylish@hotmail.com",
         subject="test correo",
         body="Mensaje de prueba"
    )
    