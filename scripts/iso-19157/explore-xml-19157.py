import xml
import xml.etree.ElementTree as ET
import re
#~ import plotly.express as px
#~ import pandas as pd
#~ import sys

#----------------------------------
# Script name
#----------------------------------
# ~ args = sys.argv
# ~ xml_report = [elt for elt in args if '.xml' in elt]
xml_report = ['xml-19157/fake-dng2.0-iso.xml']
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

print([re.sub('\\{.*\\}', '', elt.tag) for elt in root])

def getNode(node, level, inc, results):
	level = level+1
	for elt in node:
		inc = inc+1
		res = [elt.tag, elt.text, level, inc]
		results.append(res)
		getNode(elt, level, inc, results)
	return results

results = []
results = getNode(root, 0, 0, results)

print('Nombre de noeuds : %i'%len(results))

results2 = [elt for elt in results if elt[1] is not None]
print('Nombre de noeuds sans valeurs nulles (None) : %i'%len(results2))
results2 = [elt for elt in results2 if bool(re.match('\\n\\t', elt[1]))]
print('Nombre de noeuds avec des valeurs présentes : %i'%len(results2))

#~ for elt1 in root:
	#~ print(elt1.tag)
	#~ for elt2 in elt1:
		#~ print(elt2.tag)
		#~ for elt3 in elt2:
			#~ print(elt3.tag)
			#~ for elt4 in elt3:
				#~ print(elt4.tag)
				#~ for elt5 in elt4:
					#~ print(elt5.tag)
					#~ for elt6 in elt5:
						#~ print(elt6.tag)
						#~ for elt7 in elt6:
							#~ print(elt7.tag)
							#~ for elt8 in elt7:
								#~ print(elt8.tag)
								#~ for elt9 in elt8:
									#~ print(elt9.tag)
									#~ for elt10 in elt9:
										#~ print(elt10.tag)
										#~ for elt11 in elt10:
											#~ print(elt11.tag)
											#~ for elt12 in elt11:
												#~ print(elt12.tag)
												#~ for elt13 in elt12:
													#~ print(elt13.tag)
													#~ for elt14 in elt13:
														#~ print('14 > '+elt14.tag)
