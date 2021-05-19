import xml
import xml.etree.ElementTree as ET
import plotly.express as px
import pandas as pd
import sys

#----------------------------------
# Script name
#----------------------------------
# ~ args = sys.argv
# ~ xml_report = [elt for elt in args if '.xml' in elt]
xml_report = ['report-19157.xml']
if(len(xml_report) == 0):
	print("Pas de rapport XML trouvé")
	quit
else:
	xml_report = xml_report[0]
# ~ print(xml_report)
	
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
	color_discrete_map={'Conforme':'#58dd51', 'Non conforme':'#f6e3e7'})	
	fig.write_image(output_plot)
	
# render_plot
def render_plot(metric, value, valueType, output_plot):
	if(valueType=='Real'): 
		render_plot_real(metric, float(value), output_plot)
		html=("<img src=%s></img>")%(output_plot)    
		f.write(html)
	# ~ if(valueType=='Integer'): print("Integer")
	# ~ if(valueType=='Text'): print("Text")
	# ~ if(valueType=='Date'): print("Date")
	# ~ if(valueType=='Matrix'): print("Matrix")

# render_group
def render_group(group):
	# ~ print(("## %s")%(group))
	html=("<h2>%s</h2>")%(group)
	f.write(html)
		
	for elt in root.findall((".//*[@group='%s']")%(group)):
		
		metric = elt.tag
		value = elt.text
		valueType = elt.attrib["valueType"]
		
		# write values to html
		html=("<p>%s %s</p>")%(metric, value)
		f.write(html)
		
		# create plot
		output_plot = ("%s.png")%metric
		render_plot(metric, value, valueType, output_plot)	
		
# Render stars
def render_stars(nStars, n = 5) :
	nNonStars = n - nStars
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
	fig.update_traces(fill='toself', fillcolor='#58dd51', line_color = "#58dd51")
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

#-----------------------------
# Dataset
#-----------------------------

dataset = root.find('dataset').text
f.write("<h2>Dataset</h2>")
f.write(("<p>%s</p>")%dataset)

f.write('<p>')
f.write(("Date de création : %s<br>")%root.find('metrics/dateCreation').text)
f.write(("Date de révision : %s<br>")%root.find('metrics/dateRevision').text)
f.write(("Date de publication : %s<br>")%root.find('metrics/datePublication').text)
f.write('</p>')

#-------------------------------------
# users
#-------------------------------------

f.write("<div>")
f.write(("<h2>%s</h2>")%("User Advice"))

elt = root.find('users/note')

stars = render_stars(int(elt.text))
f.write(("<p>%s %s</p>")%(elt.tag, stars))
    
f.write(("<h3>%s</h3>")%("Details"))
users_details = root.find('users/details')
for elt in users_details:
	stars = render_stars(int(elt.text))
	f.write(("<p>%s %s</p>")%(elt.tag, stars))

f.write("</div>")

 

#-------------------------------------
# synthese
#-------------------------------------

f.write("<div>")
f.write(("<h2>%s</h2>")%("Dataset quality metrics"))

synthese = root.find('synthese')

labels = list()
values = list()
for elt in synthese:
	labels.append(elt.tag)
	values.append(int(elt.text))
	stars = render_stars(int(elt.text))
	f.write(("<p>%s %s</p>")%(elt.tag, stars))

render_radar(values, labels, 'radar.png')
f.write("</div>")
 

#-------------------------------------
# usages
#-------------------------------------


usages = root.find('usages')

f.write("<div>")
f.write("<h2>Metrics depending on usage</h2>")
for usage in usages:
	usageType = usage.attrib["type"]
	usageDescription = usage.attrib["description"]
	f.write(("<h3>%s</h3>")%(usageDescription))
	# ~ print(usageType)
	labels = list()
	values = list()
	for elt in usage:
		labels.append(elt.tag)
		values.append(int(elt.text))
		stars = render_stars(int(elt.text))
		f.write(("<p>%s %s</p>")%(elt.tag, stars))
	output_plot = ("radar-%s.png")%(usageType)
	render_radar(values, labels, output_plot)
f.write("</div>")

 

#-----------------------------
# metrics
#-----------------------------

f.write("<div>")
render_group("exhaustivity")
f.write("<br>")
render_group("logicalConsistency")
f.write("<br>")
render_group("positionAccuracy")
f.write("<br>")
render_group("thematicAccuracy")
f.write("<br>")
render_group("temporalAccuracy")
f.write("<br>")
render_group("genealogy")
f.write("<br>")
render_group("spatialAccuracy")
f.write("<br>")
render_group("referenDates")
f.write("</div>")

f.write("</body>")
f.write("</html>")
    
# Close file
f.close()

