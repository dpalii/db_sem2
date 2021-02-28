from lxml import etree
import codecs


root = None
fileObj = codecs.open( "results/posolstva.xml", "r", "utf_8_sig" )
root = etree.parse(fileObj)
fileObj.close()

pageUrls = root.xpath('//page/@url')
textFragmentsCount = max(map(lambda url: root.xpath(f'count(//page[@url="{url}"]/fragment[@type="text"])'), pageUrls))
print('Maximum count of text fragments amoung all pages: %d' % (textFragmentsCount))
