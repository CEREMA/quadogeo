import xml
import xml.etree.ElementTree as ET
import re
#~ import plotly.express as px
#~ import pandas as pd
import sys

#----------------------------------
# Script name
#----------------------------------
args = sys.argv
xml_report = [elt for elt in args if '.xml' in elt]
#~ xml_report = ['xml-19157/fake-dng2.0-iso.xml']
if(len(xml_report) == 0):
	print("Pas de rapport XML trouvé")
	quit
else:
	xml_report = xml_report[0]
	
#----------------------------------
# Parse XML
#----------------------------------
tree = ET.parse(xml_report)
root = tree.getroot()

node = root.find('{http://www.isotc211.org/2005/gmd}dataQualityInfo')
dqNodes = [elt for elt in root if elt.tag == '{http://www.isotc211.org/2005/gmd}dataQualityInfo']

def getTag(s):
	return re.sub('\\{.*\\}', '', s)

def getInfo(node) :
	metricId = node.tag # '{http://www.isotc211.org/2005/gmd}DQ_AbsoluteExternalPositionalAccuracy'
	descriptionEng = node.find('{http://www.isotc211.org/2005/gmd}nameOfMeasure') \
	.find('{http://www.isotc211.org/2005/gco}CharacterString').text
	
	descriptionFr = node.find('{http://www.isotc211.org/2005/gmd}nameOfMeasure') \
	.find('{http://www.isotc211.org/2005/gmd}PT_FreeText') \
	.find('{http://www.isotc211.org/2005/gmd}textGroup') \
	.find('{http://www.isotc211.org/2005/gmd}LocalisedCharacterString').text
	#~ value = node.find('{http://www.isotc211.org/2005/gmd}result').find('{http://www.isotc211.org/2005/gmd}DQ_QuantitativeResult').find('{http://www.isotc211.org/2005/gmd}value').find('{http://www.isotc211.org/2005/gco}Record').text
	
	resNode = node.find('{http://www.isotc211.org/2005/gmd}result')[0]
	
	# DQ_QuantitativeResult
	if resNode.tag == '{http://www.isotc211.org/2005/gmd}DQ_QuantitativeResult':
		value = resNode \
		.find('{http://www.isotc211.org/2005/gmd}value') \
		.find('{http://www.isotc211.org/2005/gco}Record').text
	# DQ_DescriptiveResult
	elif resNode.tag == '{http://www.isotc211.org/2005/gmd}DQ_DescriptiveResult':
		value = resNode \
		.find('{http://www.isotc211.org/2005/gmd}value') \
		.find('{http://www.isotc211.org/2005/gco}Record').text
	# DQ_ConformanceResult
	elif resNode.tag == '{http://www.isotc211.org/2005/gmd}DQ_ConformanceResult':
		value = 'NC'
	# QE_CoverageResult
	#~ gmi:QE_CoverageResult : <gco:CharacterString>Discontinuity nature over the line</gco:CharacterString>
	elif resNode.tag == '{http://www.isotc211.org/2005/gmi}QE_CoverageResult':
		value = resNode \
		.find('{http://www.isotc211.org/2005/gmi}resultContentDescription') \
		.find('{http://www.isotc211.org/2005/gmi}MI_CoverageDescription') \
		.find('{http://www.isotc211.org/2005/gmd}dimension') \
		.find('{http://www.isotc211.org/2005/gmd}MD_Band') \
		.find('{http://www.isotc211.org/2005/gmd}descriptor') \
		.find('{http://www.isotc211.org/2005/gco}CharacterString').text
	else: # !! Traiter les autres cas
		value = 'NC'
	return {'descriptionFr' : descriptionFr,
			'metricId' : getTag(metricId),
			'value' : value}
	
def getHtml(d):
	html = []
	html.append('<div>')
	html.append('<h2>%s (%s)</h2>'%(d['descriptionFr'], d['metricId']))
	html.append('<br>')
	html.append(d['value'])
	html.append('</div>')
	html.append('<br>')
	return '\n'.join(html)
		
#----------------------------------
# write html
#----------------------------------
# open file
f = open("report.html", "w")

html = """<html>
<head>
</head>
<body>"""

f.write("<html>")
f.write("<head>")
f.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">')
f.write("""<style>
.checked {
  color: orange;
}

h1 {
    color: black;
    font-size: 2em;
    line-height: 2.5em;
}

h2 {
    color: black;
    font-size: 1.5em;
    line-height: 2.5em;
    margin-bottom: 10px;
    background-image: linear-gradient(to bottom, transparent 50%, #58dd51 95%);
    display: inline;
    letter-spacing: 0.1em;
    font-weight: 700;
    /* margin-bottom: 100px; */
    padding-bottom: 2px;

}

.fa.fa-star {
    color:#bebebe;
}

.fa.fa-star.checked {
    color:#58dd51;
}


div {
    border: 1px solid #bebebe;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 .0625rem .125rem 0 rgba(0,0,0,.3);
    margin-bottom:10px;
}


body {
  font-family: Arial;
  font-size: 1.2em;
}

hr {
border: 1px solid #e4e4e4;
}
</style>
""")
f.write("</head>")
f.write("<body>")

# Title
infoNode = root.find('{http://www.isotc211.org/2005/gmd}identificationInfo')

citationNode = infoNode \
.find('{http://www.isotc211.org/2005/gmd}MD_DataIdentification') \
.find('{http://www.isotc211.org/2005/gmd}citation') \
.find('{http://www.isotc211.org/2005/gmd}CI_Citation') \

title = citationNode.find('{http://www.isotc211.org/2005/gmd}title') \
.find('{http://www.isotc211.org/2005/gco}CharacterString').text

description = citationNode.find('{http://www.isotc211.org/2005/gmd}alternateTitle')  \
.find('{http://www.isotc211.org/2005/gco}CharacterString').text

date = citationNode.find('{http://www.isotc211.org/2005/gmd}date').find('{http://www.isotc211.org/2005/gmd}CI_Date').find('{http://www.isotc211.org/2005/gmd}date').find('{http://www.isotc211.org/2005/gco}Date').text

f.write('<h1>%s</h1>'%title)
f.write('<div>')
f.write('Date : ' + date)
f.write('<br>')
f.write(description)
f.write('</div>')

for dqNode in dqNodes:
	metricNodes = [elt[0] for elt in dqNode[0] if elt.tag == '{http://www.isotc211.org/2005/gmd}report']
	for node in metricNodes:
		d = getInfo(node)
		print(d)
		html = getHtml(d)
		f.write(html)
		
# Close file
f.close()
