# language_utilities
Python script utilities for language project


# Crawler #
1. Crawler is using Python 3 and Scrapy
2. Tutorial : https://docs.scrapy.org/en/latest/intro/tutorial.html
3. Files: 
	GKvocab_n2.xml --> Source file with vocab entries
	wiki_crawl.py -> Web crawler

   Output files: 
        vocab_score_db.txt --> score for all vocab entries found in pages crawled ( 1 point per entry found )
        sentence_db.txt    --> preliminary set of example sentences
  
3. To run web_craler.py  : 
   #> scrapy runspider web_crawler.py

4. Parameters in script: 
    MAX_PAGES = 10 		--> MAX pages to crawl, keep low for testing, the number of pages crawled grows exponentially
    NEXT_PAGE_PROB = 70 	--> Probability to follow a link within the page
    BREAKPOINT = 500 		--> For graphing purposes, dump results every 500 pages crawled

WARNING: rate should be 2, otherwise we may violate wikipedia terms of use for downloading their pages
class BlogSpider(scrapy.Spider):
    rate = 2 #DO NOT CHANGE

----------------------------------------------------------------------------------------------------------
# Verb Conjugation # Script: verb_conjugate.py

Description: Takes an XML Vocab list, locates Verbs, and outputs the full conjugation table for regular verbs 

#> python3 verb_conjugate.py



----------------------------------------------------------------------------------------------------------
#Update Vocabulary # Script: update_vocabulary.py

Description: Takes a base GK vocabulary file format, checks against the JDICT ( dictionary ) and updates the entry with JDICT definitions ( up to 4)  POS, Verb types, notes, and tags.

PARAMETERS: 
INPUT_FILENAME = "./GKvocab_n3.xml"      #filename to modify
DICT_FILENAME = "/tools/dict/JMdict_e"   #location of the JDICT dictionary
OUTPUT_FILENAME = "GK3_updated.xml"	 #Updated filename

#> python3 update_vocabulary.py
