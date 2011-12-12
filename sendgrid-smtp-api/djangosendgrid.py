"""
sendgrid.py
-----------
Implements SendGrid's SMTP api and provdes a Django send_mail replacement 

Usage
------
import send_mail_with_headers as send_mail and your existing send_mail calls 
will work with SendGrid. To set headers, create a SendGridApiHeader and pass it
to the send_mail_with_headers function.

License: Triple licensed under the GNU GPL v2, GNU GPL v3 and MIT License

Contributors:

- Mike Seidle -- http://directemployersfoundation.org
  mike@directemployersfoundation.org
"""

from django.core import mail


def send_mail_with_headers(subject, message, from_email, recipient_list,
                           fail_silently=False, auth_user=None,
                           auth_password=None, connection=None,
                           headers=None):
    """Allows Django to send mail via SendGrid with SendGrid SMTP API headers.
       
       If you import this as send_mail, your existing Django using 
       django.mail.send_mail with work with sendgrid. 
       
       Parameters:
       
       - subject -- Subject of message
       - message -- Actual message
       - from_email -- email address that message is from
       - recipient_list -- list of recipients ['joe@test.com','bill@test.com...]
       - fail_silently -- True or False
       - auth_user -- SMTP user. Uses ettings.py default.
       - auth_password -- Password for SMTP user. Uses settings.py default.
       - connection -- a django.mail.connection 
       - headers -- an dict containing a properly formatted sendgrid API header
                    ordinarily some_smt_papi_header.as_django_smtp_header()
       
       """
    
    connection = connection or mail.get_connection(username=auth_user,
            password=auth_password, fail_silently=fail_silently)
    # set headers if headers are not supplied.
    headers = headers or {}
    # Make sure we have some headers set
    # form the message with headers.
    message = mail.EmailMessage(subject, message, from_email, recipient_list,
        connection=connection, headers=headers.as_django_email_header)
    connection.send_messages([message])
