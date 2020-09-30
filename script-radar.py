import plotly.express as px
import pandas as pd
import xml
import xml.etree.ElementTree as ET
import plotly.express as px
import pandas as pd
import sys

tree = ET.parse('report.xml')
root = tree.getroot()

# Synthese et radar
synthese = root.find('synthese')
labels = list()
values = list()
for elt in synthese:
	print(elt)
	labels.append(elt.tag)
	values.append(int(elt.text))

print(labels)
print(values)	

df = pd.DataFrame(dict(
    r=values,
    theta=labels))
    
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.write_image('radar.png')
