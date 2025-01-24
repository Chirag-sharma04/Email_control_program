import smtplib
import imaplib
import email
import os

class EmailControl:
    def __init__(self, email_user, email_password):
        self.email_user = email_user
        self.email_password = email_password
        self.imap_host = 'imap.gmail.com'  # Change for other providers
        self.smtp_host = 'smtp.gmail.com'  # Change for other providers

    def connect_imap(self):
        self.mail = imaplib.IMAP4_SSL(self.imap_host)
        self.mail.login(self.email_user, self.email_password)

    def connect_smtp(self):
        self.smtp = smtplib.SMTP_SSL(self.smtp_host, 465)
        self.smtp.login(self.email_user, self.email_password)

    def read_emails(self, folder='inbox'):
        self.mail.select(folder)
        result, data = self.mail.search(None, 'ALL')
        email_ids = data[0].split()
        emails = []
        for e_id in email_ids:
            result, msg_data = self.mail.fetch(e_id, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])
            emails.append(msg)
        return emails

    def reply_to_email(self, original_email, reply_content):
        reply = email.message.EmailMessage()
        reply['Subject'] = 'Re: ' + original_email['Subject']
        reply['From'] = self.email_user
        reply['To'] = original_email['From']
        reply.set_content(reply_content)
        self.smtp.send_message(reply)

    def send_email(self, to, subject, content):
        msg = email.message.EmailMessage()
        msg['From'] = self.email_user
        msg['To'] = to
        msg['Subject'] = subject
        msg.set_content(content)
        self.smtp.send_message(msg)

    def move_to_inbox(self, email_id):
        self.mail.copy(email_id, 'INBOX')
        self.mail.store(email_id, '+FLAGS', '\\Deleted')
        self.mail.expunge()

    def close_connections(self):
        self.mail.logout()
        self.smtp.quit()

# Example usage
if __name__ == "__main__":
    email_user = 'your_email@gmail.com'
    email_password = 'your_password'
    email_control = EmailControl(email_user, email_password)
    
    email_control.connect_imap()
    email_control.connect_smtp()
    
    # Read emails
    emails = email_control.read_emails()
    for email in emails:
        print(email['From'], email['Subject'])
    
    # Send a test email
    email_control.send_email('recipient@example.com', 'Test Subject', 'Test Content')
    
    # Close connections
    email_control.close_connections()
