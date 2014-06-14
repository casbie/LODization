#-*- coding: utf-8 -*-
import csv

source_list=['呂勝由','特稀圖','FOT','特稀有','賴明洲','渡假','文建會','教育廳','蘇鴻傑1','蘇鴻傑2']
family_name=''

def read_input_data(filename):
	fp=open(filename,'r')
	fp_out=open("Taiwan_Redlist.rdf",'w')
	
	for row in csv.DictReader(fp):

		species_number=row['編號']
		resource_uri='http://lod.ac/redlist/readlist-taiwan-'+species_number

		science_name=row['學名'].strip()
		science_name_label=science_name
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
		
		if science_name.isupper(): #is family name
			family_name=science_name.lower().capitalize()
			sub='<http://lod.ac/species/'+family_name+'>'
			pre='speciesOnto:hasCommonName'
			obj='<http://lod.ac/species/'+chinese_name+'>'
			fp_out.write(sub+' '+pre+' '+obj+'.\n')

			sub=obj
			pre='rdfs:label'
			obj='\"'+chinese_name+'\"@zh'
			fp_out.write(sub+' '+pre+' '+obj+'.\n')
			continue
		
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

		#information of scientific name
		sub='<http://lod.ac/species/'+science_name+'>'
		information=[]
		
		pre='a'
		obj='speciesOnto:ScientificName'
		information.append((pre,obj))

		pre='speciesOnto:hasCommonName'
		obj='<http://lod.ac/species/'+chinese_name+'>'
		information.append((pre,obj))

		pre='speciesOnto:hasSuperTaxon'
		obj='<http://lod.ac/species/'+family_name
		information.append((pre,obj))

		pre='rdfs:label'
		obj='\"'+science_name_label+'\"'
		information.append((pre,obj))
		
		pre='cnsvOnto:hasRedListEntry'
		obj='redlist:readlist-taiwan-'+species_number
		information.append((pre,obj))
		
		fp_out.write(sub+'\n')
		for i in information:
			fp_out.write('\t'+i[0]+' '+i[1])
			if d != descriptions[-1]:
				fp_out.write(';\n')
			else:
				fp_out.write(' .\n')

		#fp_out.write(sub+' '+pre+' '+obj+' .\n')

		#information of common name
		sub='<http://lod.ac/species/'+chinese_name+'>'
		pre='rdfs:label'
		obj='\"'+chinese_name+'\"@zh'
		fp_out.write(sub+' '+pre+' '+obj+' .\n')
	fp.close()

if __name__=='__main__':
	read_input_data("RedList.csv")
