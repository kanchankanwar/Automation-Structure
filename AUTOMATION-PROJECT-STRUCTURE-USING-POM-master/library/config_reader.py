import configparser

def readconfigdata(section, key):
    c = configparser.ConfigParser()
    c.read("./config/config.cfg")
    return c.get(section, key)

#print(readconfigdata('details','Application_URL'))

def fetch_element(section, key):
    c = configparser.ConfigParser()
    c.read("./config/elements.cfg")
    return c.get(section, key)