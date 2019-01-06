import sendgrid
from sendgrid.helpers.mail import *

def Send_Email(to_email,msg_body):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email("suryaspeed@gmail.com")
    to_email = Email(to_email)
    subject = "QREG Data"
    content = Content("text/plain",msg_body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)

