import xml.dom.minidom
from xml.dom import pulldom

# Load the XML document
dom = xml.dom.minidom.parse('movies.xml')

# Load the DTD
parser = pulldom.DOMParser()
dtd = parser.parse('DTD.dtd')

# Validate the document against the DTD
for event, node in dtd:
    if event == pulldom.START_DOCUMENT:
        continue
    if event == pulldom.END_DOCUMENT:
        break
    if event == pulldom.DTD:
        continue
    if event == pulldom.START_ELEMENT:
        if not dtd.match(node):
            print("XML document is not valid against the DTD.")
            break

print("XML document is valid against the DTD.")
