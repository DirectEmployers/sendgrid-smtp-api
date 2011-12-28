SendGrid SMTP API & Django Helpers
==================================
Cleaned up version of SendGrid's SMTP API code with a simple function that 
allows Django developers to replace django.mail.send_mail with a send_mail that
allows the SendGrid SMTP API to be used.


Copyright and License
---------------------
Copyright (C) 2011, DirectEmployers Foundation.  This project is provided under
a triple license that allows you to select the license that is best for your 
needs. You may choose from:

- The GNU GPL v2.0
- The GNU GPL v3.0
- The MIT License

You can read the license text at:
http://directemployersfoundation.org/tri-license

How SendGrid's SMTP API Works
-----------------------------
When you send mail, you add an additional header to the message called 
X-SMTPAPI containing a JSON object that contains everything SendGrid needs to 
know to properly format, tag and deliver your messages.

Using with Python Applications
------------------------------
1. Create a SendGridApi object.
2. Create your message however you like to.
2. Add an SMTP header called X-SMTPAPI. The header should contain 
   SendGridApi.__str__() or SendGridAPI.as_json()
3. Send it.

Using with Django
-----------------
Just add:

import sendgrid
from djangosendgrid import send_mail_with_headers as send_mail

You can just copy the two files into your project or app.  At some point 
I'll package these up so they can be installed from PyPi.

Contributors
------------
SendGrid -- http://sendgrid.com - initial example Python API implementation
Mike Seidle -- mike@directemployersfoundation.org - This version

How to Contribute
-----------------
1. Clone the project from GitHub.
2. Make it better (make sure you add yourself to the contributors above)
3. Submit a Pull request on GitHub.
4. ???
5. Profit (or something)