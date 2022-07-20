"""

simple function to send an email via gmail and smtp. 
to send to multiple recipients, include a list of addresses in 
the 'to' parameter. if the recipients list includes an sms gateway address,
a group text will be sent instead. should probably split regular email from
sms when sending.

docs: 
https://docs.python.org/3/library/smtplib.html
https://docs.python.org/3/library/email.html

"""

import smtplib
from email.mime.text import MIMEText

# configured to use gmail, for 'key', generate an app key and use that. 
from_ = "fromAddress@example.com"
key = "AppKeyHere"

def sendmail(to, subject, text):
    try:
        # create message object
        msg = MIMEText(text)
        msg['From'] = from_
        msg['Subject'] = subject

        # join list items with a comma to make an RFC 822 to-address string
        msg['To'] = ", ".join(to)
        
        # create server object, SMTP via gmail
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        
        # login to smtp server
        server.login(from_, key)
        
        # send message object
        server.send_message(msg)
    except smtplib.SMTPException:
        print("There was a problem sending the email.")
    finally:
        server.quit()
