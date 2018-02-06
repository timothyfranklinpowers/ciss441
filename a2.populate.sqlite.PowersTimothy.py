import json
import csv
import sqlite3
import sys

dbfile = 'flavors_of_cacao.db' #the database file
conn = sqlite3.connect(dbfile) #connect to the database

def main():
	create_table()	#create the table
	open_file()		#open file
	print('Got it!')#confirmation
	conn.close()	#close the connection
	sys.exit(1)		#a gentle exit
	
def create_table():
	"""This table is where the csv is going to be loaded to"""
	c = conn.cursor()
	strsql="""
		CREATE TABLE if not exists cacao (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			Company text,
			Specific_Bean_Origin text,
			REF	int,
			Review	int,
			Cocoa text,
			Location text,
			Rating	float,
			Bean text,
			Broad_Bean_Origin text
			);
		"""
	c.execute(strsql)
	conn.commit()
	
def open_file():
	"""open the csv file and load into the cacao table """
	r_ct = 0
	
	with open('flavors_of_cacao.csv', 'r') as csvfile:
		cacao_stream = csv.DictReader(csvfile)
		for cacao_row in cacao_stream:
			r_ct += 1
			
			#quit after 100 records
			if r_ct > 100:
				break
				
			#pull the data out of the dictionary for sqlite3
			t_Company = cacao_row['Company']
			t_Specific_Bean_Origin = cacao_row['Specific_Bean_Origin']
			t_REF = cacao_row['REF']
			t_Review = cacao_row['Review']
			t_Cocoa = cacao_row['Cocoa']
			t_Location = cacao_row['Location']
			t_Rating = cacao_row['Rating']
			t_Bean = cacao_row['Bean']
			t_Broad_Bean_Origin = cacao_row['Broad_Bean_Origin']
			
			#print the first 15 lines
			if r_ct <= 15:
				print (r_ct, t_Company, t_Bean, t_Cocoa, t_Review)
				
			#creates a sql cursor, formats the insert sql and executes it
			c = conn.cursor()
			strsql = """
				INSERT INTO cacao
					(Company, Specific_Bean_Origin, REF, Review, Cocoa, Location, Rating, Bean, Broad_Bean_Origin)
				values (
					'{t_Company}', '{t_Specific_Bean_Origin}', '{t_REF}', '{t_Review}', '{t_Cocoa}', '{t_Location}', '{t_Rating}', '{t_Bean}', '{t_Broad_Bean_Origin}');
				""".format(
					t_Company = t_Company,
					t_Specific_Bean_Origin = t_Specific_Bean_Origin,
					t_REF = t_REF,
					t_Review = t_Review,
					t_Cocoa = t_Cocoa,
					t_Location = t_Location,
					t_Rating = t_Rating,
					t_Bean = t_Bean,
					t_Broad_Bean_Origin = t_Broad_Bean_Origin
					)
			c.execute(strsql)
			conn.commit()

			
if __name__ == "__main__":
	main()