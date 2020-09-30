import xml
import xml.etree.ElementTree as ET
import plotly.express as px
import pandas as pd
import sys

#----------------------------------
# Script name
#----------------------------------
args = sys.argv
xml_report = [elt for elt in args if '.xml' in elt]
if(len(xml_report) == 0):
	print("Pas de rapport XML trouvé")
	quit
else:
	xml_report = xml_report[0]
print(xml_report)
	
#----------------------------------
# Parse XML
#----------------------------------
tree = ET.parse(xml_report)
root = tree.getroot()

#----------------------------------
# Fonctions
#----------------------------------

# render_plot_real
def render_plot_real(metric, value, output_plot):
	data = {'values':  [value, 1-value], 'labels' : ['Conforme', 'Non conforme']}
	df = pd.DataFrame(data)
	fig = px.pie(df, values='values', names='labels', title=metric, 
	color='labels', 
	color_discrete_map={'Conforme':'lightblue', 'Non conforme':'lightcoral'})	
	fig.write_image(output_plot)
	
# render_plot
def render_plot(metric, value, valueType, output_plot):
	if(valueType=='Real'): 
		render_plot_real(metric, float(value), output_plot)
		html=("<img src=%s></img>")%(output_plot)    
		f.write(html)
	if(valueType=='Integer'): print("Integer")
	if(valueType=='Text'): print("Text")
	if(valueType=='Date'): print("Date")
	if(valueType=='Matrix'): print("Matrix")

# render_group
def render_group(group):
	print(("## %s")%(group))
	html=("<h2>%s</h2>")%(group)
	f.write(html)
		
	for elt in root.findall((".//*[@group='%s']")%(group)):
		
		metric = elt.tag
		value = elt.text
		valueType = elt.attrib["valueType"]
		
		# write values to html
		html=("<p>%s : %s</p>")%(metric, value)
		f.write(html)
		
		# create plot
		output_plot = ("%s.png")%metric
		render_plot(metric, value, valueType, output_plot)	
		
# Render stars
def render_stars(nStars) :
	nNonStars = 10 - nStars
	elt_checked = '<span class="fa fa-star checked"></span>'
	elt_notChecked = '<span class="fa fa-star"></span>'
	elts_checked = '\n'.join([elt_checked]*nStars)
	elts_notChecked = '\n'.join([elt_notChecked]*nNonStars)
	elts = "%s%s"%(elts_checked, elts_notChecked)
	return(elts)


# Radar data frame
def render_radar(values, labels, output_plot):

	df = pd.DataFrame(dict(
		r=values,
		theta=labels))
		
	fig = px.line_polar(df, r='r', theta='theta', line_close=True)
	fig.update_traces(fill='toself')
	fig.update_layout(
		polar=dict(
		radialaxis=dict(
			visible=True,
		range=[0, 10]
		)))
	fig.write_image(output_plot)
	
	f.write(("<img src='%s'></img>")%(output_plot))

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
</style>
""")
f.write("</head>")
f.write("<body>")
f.write("<h1>QuaDoGeo Report</h1>")

#-----------------------------
# Radar métriques calculées
#-----------------------------
print("## Radar métriques calculées")

f.write(("<h2>%s</h2>")%("Indicateurs de qualité calculés"))

synthese = root.find('synthese')

labels = list()
values = list()
for elt in synthese:
	labels.append(elt.tag)
	values.append(int(elt.text))
	stars = render_stars(int(elt.text))
	f.write(("<p>%s : %s</p>")%(elt.tag, stars))
print(labels)
print(values)	

render_radar(values, labels, 'radar.png')


#-----------------------------
# Radar métriques nécessaires
#-----------------------------

print("## Radars selon usages")

usages = root.find('usages')

for usage in usages:
	usageType = usage.attrib["type"]
	usageDescription = usage.attrib["description"]
	f.write(("<h2>%s</h2>")%(usageDescription))
	print(usageType)
	labels = list()
	values = list()
	for elt in usage:
		labels.append(elt.tag)
		values.append(int(elt.text))
		stars = render_stars(int(elt.text))
		f.write(("<p>%s : %s</p>")%(elt.tag, stars))
	print(labels)
	print(values)
	output_plot = ("radar-%s.png")%(usageType)
	render_radar(values, labels, output_plot)


#-----------------------------
# Render metrics
#-----------------------------
render_group("exhaustivity")
render_group("logicalConsistency")
render_group("positionAccuracy")
render_group("thematicAccuracy")
render_group("temporalAccuracy")
render_group("genealogy")
render_group("spatialAccuracy")
render_group("referenDates")

f.write("</body>")
f.write("</html>")
    
# Close file
f.close()

