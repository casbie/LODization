#-*- coding: utf-8 -*-
import csv

source_list=['呂勝由','特稀圖','FOT','特稀有','賴明洲','渡假','文建會','教育廳','蘇鴻傑1','蘇鴻傑2']

def read_input_data(filename):
	fp=open(filename,'r')
	fp_out=open("Taiwan_Redlist.rdf",'w')
	
	for row in csv.DictReader(fp):
		species_number=row['編號']
		resource_uri='http://lod.ac/redlist/readlist-taiwan-'+species_number

		science_name=row['學名']
		temp=science_name.split(' ')
		if temp>1:
			science_name=''
			for part in temp:
				if part == '':
					break
				science_name=science_name+part+'_'
			science_name=science_name[:-1]

		chinese_name=row['中名']
		evaluation=row['評估']
		#source=[]
		#number=0
		#for s in source_list:
		#	source.append(row[s])
		#	number=number+1
		
		descriptions=[]
		
		descriptions.append(('http://lod.ac/ns/cnsv#ofSpecies',science_name))
		descriptions.append(('http://lod.ac/ns/cnsv#ofArea','台灣 @zh'))
		if evaluation:
			descriptions.append(('http://lod.ac/ns/cnsv#currentStatus',evaluation))
		for s in source_list:
			if row[s]:
				descriptions.append(('http://lod.ac/ns/cnsv#currentStatus',s+'_'+row[s]))

		fp_out.write('<'+resource_uri+'>'+'\n')
		for d in descriptions:
			fp_out.write('\t<'+d[0]+'> \"'+d[1]+'\"')
			if d != descriptions[-1]:
				fp_out.write(';\n')
			else:
				fp_out.write(' .\n')

	fp.close()

if __name__=='__main__':
	read_input_data("RedList.csv")
