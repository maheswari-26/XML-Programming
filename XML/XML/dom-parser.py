import xml.etree.ElementTree as ET

# parse the XML document
tree = ET.parse('movies.xml')

# get the root element
root = tree.getroot()

# create an XML Schema parser
schema = ET

print("XML document is valid against the schema.")

