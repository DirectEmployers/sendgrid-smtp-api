# tests.py -- Test suite for sendgrid
import unittest2 

from sendgrid import SmtpApiHeader

class SmtpApiTest(unittest2.TestCase):
    """Test suite for SendGrid smpt header object"""

    def test_smtpaipheader_addCategory(self):
        """Test SendGrid SMTP Header with just a category."""
        h = SmtpApiHeader()
        h.set_category("Transactional")
        # we are testing a string against a string
        self.assertEqual(h.__str__(),
                         'X-SMTPAPI: {"category": "Transactional"}')

    def test_smtpapiheader_addTo(self):
        """Test SendGrid SMTP header with recipients"""
        expected = 'X-SMTPAPI: {"to": ["kyle@somewhere.com", ' + \
            '"bob@someplace.net", "someguy@googlemailz.coms"]}'
        tos = ['kyle@somewhere.com',
               'bob@someplace.net',
               'someguy@googlemailz.coms']
        h = SmtpApiHeader()
        h.add_to(tos)
        # remember we are testing a string against a string
        self.assertEqual(h.__str__(), expected)

    def test_smtpapiheader_setUniqueArgs(self):
        """Test SendGrid SMTP Header unique args"""
        expected = 'X-SMTPAPI: {"unique_args": {"testa": 1, "testb": 2}}'
        h = SmtpApiHeader()
        h.set_unique_args({'testa': 1, 'testb': 2})
        self.assertEqual(h.__str__(), expected)

    def test_smtpapiheader_asjson(self):
        """Test SendGrid SMTP headers work as JSON"""
        expected = '{"category": "Transactional"}'
        h = SmtpApiHeader()
        h.set_category("Transactional")
        # yes, it says asJSON, but it's a string of JSON not a JSON object
        self.assertEqual(h.as_json(), expected)

    def test_smtpapiheader_as_django_header(self):
        """Test django ready email header dict."""
        expected = {'X-SMTPAPI': '{"category": "foo", "filters": {"category": {"settings": {"setting": "value"}}}}'}
        h = SmtpApiHeader()
        h.set_category('foo')
        h.add_filter_setting('category', 'setting', 'value')
        self.assertEqual(h.as_django_email_header(), expected)

if __name__ == '__main__':
    unittest2.main()