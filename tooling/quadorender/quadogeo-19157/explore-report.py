import xml
import xml.etree.ElementTree as ET
import pandas as pd
import sys

#----------------------------------
# Script name
#----------------------------------
xml_iso = 'report-19157.xml'

#----------------------------------
# Parse XML
#----------------------------------
tree = ET.parse(xml_iso)
root = tree.getroot()
