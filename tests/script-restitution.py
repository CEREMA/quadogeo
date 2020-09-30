# Rajouter les types au XML
# 

import xml
import xml.etree.ElementTree as ET
import matplotlib
import matplotlib.pyplot as plt

tree = ET.parse('quadogeo.xml')

# ROOT
root = tree.getroot()

print(root.tag)

print(root.attrib)

# TAUX
print("children")
taux = root.find('taux')
libelles = list()
values = list()
for child in taux:
	print(child.tag, child.attrib)
	print("single")
	libelles.append(child.tag)
	values.append(float(child.text))

print(libelles)
print(">> values : ", values)
	
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(libelles, values)
plt.show()

# misc	
print([elem.tag for elem in root.iter()])

# tostring
print(ET.tostring(root, encoding='utf8').decode('utf8'))

# Indicateur 5
synthese = root.find('synthese')

