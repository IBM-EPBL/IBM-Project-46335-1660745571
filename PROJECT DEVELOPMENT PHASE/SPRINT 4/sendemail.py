import smtplib
import sendgrid as sg
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "CUSTOMER CARE REGISTRY"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
    s.login("keerthana.selvaraj2019@kgkite.ac.in", "keerthigk@123106")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    
    s.sendmail("keerthana.selvaraj2019@kgkite.ac.in", email, message)
    s.quit()
def sendgridmail(user,TEXT):
  
    
    from_email = Email("keerthana.selvaraj2019@kgkite.ac.in") 
    to_email = To(user) 
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)

    

    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)