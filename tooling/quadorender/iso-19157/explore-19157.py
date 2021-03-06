import xml
import xml.etree.ElementTree as ET
import pandas as pd
import sys

#----------------------------------
# Script name
#----------------------------------
xml_iso = '19157/-2/mdq/1.0/dataQualityElement.xsd'

#----------------------------------
# Parse XML
#----------------------------------
tree = ET.parse(xml_iso)
root = tree.getroot()

#----------------------------------
# Explore
#----------------------------------

# Tags
tags = list(set([elt.tag for elt in root]))
print(tags)

# Iterate
nodes = [elt for elt in root if elt.tag in ['{http://www.w3.org/2001/XMLSchema}element']]

for elt in nodes:
    if 'element' in elt.tag:
        print('element')
    elif 'complexType' in elt.tag:
        print('complexType')
    print(elt.attrib['name'])

# ComplexTypes
for elt in root.iter('{http://www.w3.org/2001/XMLSchema}complexType'):
    print(elt)
