import smtplib
from email.message import EmailMessage

class EmailSender:
    
    def __init__(self, smtp_password: str, send_to: str, subject: str, body: str) -> None:
        """
        Initializes the EmailSender object.

        Args:
            smtp_password (str): The password for the SMTP server.
            send_to (str): The email address to send the email to.
            subject (str): The subject line of the email.
            body (str): The body of the email.

        Returns:
            None.

        """
        self.SMTP_SERVER = 'smtp.hostnet.nl'
        self.SMTP_PORT = 587
        self.SMTP_USERNAME = 'dev@flowerofmine.nl'
        self.SMTP_PASSWORD = smtp_password
        self.send_to = send_to
        self.subject = subject
        self.body = body
        self.msg= self.create_message()

    def create_message(self):
        """
        Creates an email message.

        Returns:
            msg (EmailMessage): The email message.

        """
        msg = EmailMessage()
        msg.set_content(self.body)
        msg['Subject'] = self.subject
        msg['From'] = self.SMTP_USERNAME
        msg['To'] = self.send_to
        return msg

    def send(self):
        """
        Sends the email.

        Returns:
            None.

        """
        connection = smtplib.SMTP(host=self.SMTP_SERVER, port=self.SMTP_PORT)
        connection.starttls()
        connection.login(user=self.SMTP_USERNAME, password=self.SMTP_PASSWORD)
        connection.send_message(self.msg)
        connection.close()

