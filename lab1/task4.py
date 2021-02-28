import lxml.etree as ET


def xslt_parse():
    dom = ET.parse('results/odissey.xml')
    xslt = ET.parse('odissey.xslt')
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    with open('results/odissey.html', 'wb') as f:
        f.write(ET.tostring(newdom, pretty_print=True))

xslt_parse()
