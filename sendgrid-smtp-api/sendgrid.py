"""
sendgrid.py

Implements SendGrid's SMTP api and provdes a Django send_mail replacement 

License: Tri-licensed under the GNU GPL2, GNU GPL3 and MIT License.

Authors:

- SendGrid.com -- http://sendgrid.com
- Mike Seidle -- http://directemployersfoundation.org
                 mike@directemployersfoundation.org
  
"""

import json
import re


class SmtpApiHeader:
    """Creates mail header for SendGrid SMTP API

    Creates folded X-SMTPAPI header for passing settings to the SendGrid
    SMTP API.

    Documentation for the SendGrid API is available at:
    http://docs.sendgrid.com/documentation/api/smtp-api/
    """

    def __init__(self):
        self.data = {}

    def add_to(self, recipient):
        """Adds a list of recipients

        Arguments:

        - to -- a list of email addresses
        """

        if 'recipient' not in self.data:
            self.data['to'] = []
        if type(recipient) is str:
            self.data['to'] += [recipient]
        else:
            self.data['to'] += recipient

    def add_sub_val(self, var, val):
        """Adds substitution values to SendGrid header

        Substitution values are inserted into the body of the message
        where <% %> tags appear. Values must be set for each recipient
        address. Arguments:

        - var -- name of substitution tag
        - val -- list of values for the tag for each recipient.
        """

        if 'sub' not in self.data:
            self.data['sub'] = {}
        if type(val) is str:
            self.data['sub'][var] = [val]
        else:
            self.data['sub'][var] = val

    def set_unique_args(self, val):
        """Sets Unique Argument for all emails.

        Arguments:

        - val -- a dictionary of unique values. eg. {"batch": "200"}
        """

        if type(val) is dict:
            self.data['unique_args'] = val

    def set_category(self, cat):
        """Adds a category to the SendGrid header
        
        Arguments:
        
        - cat -- string containing category
        """
        self.data['category'] = cat

    def add_filter_setting(self, fltr, setting, val):
        """ Adds a filter setting header. Filter = Sendgrid app setting.
        
        Arguments 
        
        - fltr -- The name of the SendGrid App
        - setting -- The SendGrid App  setting being changed
        - value -- The actual value of the setting.
        """
        
        if 'filters' not in self.data:
            self.data['filters'] = {}
        if fltr not in self.data['filters']:
            self.data['filters'][fltr] = {}
        if 'settings' not in self.data['filters'][fltr]:
            self.data['filters'][fltr]['settings'] = {}
        self.data['filters'][fltr]['settings'][setting] = val

    def as_json(self):
        """ Returns Sendgrid API settings as JSON."""

        j = json.dumps(self.data)
        return re.compile('(["\]}])([,:])(["\[{])').sub('\1\2 \3', j)

    def as_string(self):
        """returns an X-SMTPAPI header string

        __str__ is more pythonic, this is kept for compatiblity with
        SendGrid's existing documentation.
        """

        j = self.as_json()
        result = 'X-SMTPAPI: %s' %  j
        return result

    def as_django_email_header(self):
        """returns X-SMTPAPI JSON in a way Django can use"""
        
        key = "X-SMTPAPI"
        value = self.as_json()
        return {key: value}

    def __str__(self):
        """returns sendgrid api X-SMTPAPI header as a string.

        Note: Calls as_string in case something is looking for
        __str__.
        """

        return self.as_string()
