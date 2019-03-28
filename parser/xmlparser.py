from lxml import etree
import uuid
from cacheout import Cache

class XMLParser():
    def __init__(self, path):
        self.cache = Cache()
        self.root = etree.parse(
            r'{0}'.format(path))

    def storeElementWithKey(self, element):
        udid = str(uuid.uuid4())
        self.cache.set(udid, element)
        return udid;

    def getStorElementWithKey(self, udid):
        print(udid)
        return self.cache.get(udid)

    def getElementByXpath(self, xpath):
        var = self.root.xpath(xpath)
        return self.storeElementWithKey(var)




