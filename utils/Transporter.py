class Transporter(object):
    """ """

    def __init__(self, name, inn, addr, phones, contacts, transporters):
        self.name = name.strip()
        self.inn = inn.strip()
        self.addr = addr.strip()
        self.phones = phones.strip().replace('\r',' ').replace('\n',' ')
        self.contacts = contacts.strip().replace('\r',' ').replace('\n',' ')
        self.transporters = transporters.strip().replace('\r',' ').replace('\n',' ')
