Data Example
==
### for each record
<http://lod.ac/redlist/readlist-taiwan-1>  
	<http://lod.ac/ns/cnsv#ofSpecies> <http://lod.ac/species/Acrostichum_aureum>;  
	<http://lod.ac/ns/cnsv#ofArea> "台灣"@zh;  
	<http://lod.ac/ns/cnsv#currentStatus> "http://lod.ac/cnsv/呂勝由_EN(II)";  
	<http://lod.ac/ns/cnsv#currentStatus> "http://lod.ac/cnsv/渡假_III";  
	<http://lod.ac/ns/cnsv#currentStatus> "http://lod.ac/cnsv/文建會_III";  
	<http://lod.ac/ns/cnsv#currentStatus> "http://lod.ac/cnsv/教育廳_III" .  

### for each species
<http://lod.ac/species/Acrostichum_aureum> a speciesOnto:ScientificName;  
	speciesOnto:hasCommonName <http://lod.ac/species/鹵蕨>;  
	speciesOnto:hasSuperTaxon <http://lod.ac/species/Adiantaceae>;  
	rdfs:label "Acrostichum aureum";  
	cnsvOnto:hasRedListEntry redlist:readlist-taiwan-1.  
	<http://lod.ac/species/鹵蕨> rdfs:label “鹵蕨”@zh.  

### for species
<http://lod.ac/species/Adiantaceae> speciesOnto:hasCommonName <http://lod.ac/species/鐵線蕨科>.  
<http://lod.ac/species/鐵線蕨科> rdfs:label “鐵線蕨科”@zh.  

File description
==
- LODredlist.py: To change the data from csv to rdf
- RedList.csv: source data
- Taiwan_Redlist.rdf: target data

Data sources
==
- 台灣維管束植物紅皮書 http://www.tsps.org.tw/redbook.htm
