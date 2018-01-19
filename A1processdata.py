# Assignment: A1
# Name: Timothy Powers

import csv
import json

row_count = 0
terrorism_data = []

# importing the csv file: each row is a list
with open('terrorism.csv', 'r') as csvfile:
	terrorism_stream = csv.DictReader(csvfile, delimiter=',', quotechar='"')
	
	# moves over the data by row
	for terrorism_row_dict in terrorism_stream:
		
		row_count += 1
		
		if row_count <= 10:
			print(row_count, terrorism_row_dict['iyear'], terrorism_row_dict['country_txt'], terrorism_row_dict['city'])
		
		terrorism_data.append(terrorism_row_dict)
		
print('There are this many rows:', row_count)
# converts and dumps to JSON
with open('result.json', 'w') as fp:
	json.dump(terrorism_data, fp, sort_keys=True, indent=4, separators=(',', ': '))
