import imp  # Deprecated since Python 3.4, removed in 3.12+

def load_mail_module(path):
    return imp.load_source('mail_module', path)

def send_mail(address, message):
    print "Sending mail to %s" % address   # Python 2 syntax
    print message
