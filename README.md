# wikipedia_postgres
load wikipedia xml datadump into postgres for analysis  

I split the file into 50 chunks to make it manageable on a smaller system.  
split -n 50 enwiki-20190301-pages-articles-multistream.xml  

It takes about 5 hours with 9 cores, 64GB, 600GB 15K sas.  
