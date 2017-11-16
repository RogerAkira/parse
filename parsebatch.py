import sys
import csv
import os
import struct



#-------------------------
print ('xmlparser')
#-------------------------


#Path to xml files
xml = 'D:/AudioDataBase/160607VBTNLURecordings/VBTNLURecordings/xmlparseall.csv'
xmlpath = 'D:/AudioDataBase/160607VBTNLURecordings/VBTNLURecordings/'
csvwrite = 'D:/AudioDataBase/csvwriteall.csv'


with open(xml, 'rb') as f:
	reader = csv.reader(f)
	row = reader.next()
	try:
		for row in reader:
			xmlfilename = os.path.normpath(os.path.join(xmlpath, row[0]))
			print xmlfilename
			print xml
			print xmlpath
			#print row[0]
			import xml.etree.ElementTree as ET
			tree = ET.parse(xmlfilename)
			#root = tree.getroot()

			for user in tree.findall('User'):
				name = user.find('Name').text
				age = user.find('Age').text
				gender = user.find('Gender').text
				accent = user.find('Accent').text
					
				print name, age, gender, accent
					
			for utterance in tree.findall('Utterance'):
				utter = utterance.text			
				print utter
				
				
			# for info in tree.findall('Info'):
				# rec = info.find('Recorded')		
				# print rec



				
						
			with open(csvwrite, 'a') as f:
				writer = csv.writer(f) #delimiter = ',')
				
				writer.writerow([name + ', '+ age + ', ' + gender + ', ' +accent + ', '+ utter])
				#writer.writerow(\n)
									
				# writer.writerows(age  )
					
				# writer.writerows(gender )
				# writer.writerows(accent )
				
				# writer.writerows(utter )
				
				
	except ValueError:
		print('opps')	
				
				
				
				
				
				
		
	
	
