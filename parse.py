import xml.etree.ElementTree as ET
tree = ET.parse('C:\Python27\parse\AB_20160602161501.xml')
root = tree.getroot()

for user in root.findall('User'):
	name = user.find('Name').text
	age = user.find('Age').text
	gender = user.find('Gender').text
	accent = user.find('Accent').text
	
	print name, age, gender, accent
	
for utterance in root.findall('Utterance'):
	
	print utterance.text