import re
import xml.etree.ElementTree as metree
import random

verb_switch = {
"VERB_5_BU": "Godan verb with `bu' ending" ,
"VERB_5_GU": "Godan verb with `gu' ending" ,
"VERB_5_KU": "Godan verb with `ku' ending" ,
"VERB_5_MU": "Godan verb with `mu' ending" ,
"VERB_5_RU": "Godan verb with `ru' ending" ,
"VERB_IRREGULAR": "Irregular Verb" ,
"VERB_5_SU": "Godan verb with `su' ending"  ,
"VERB_5_TSU": "Godan verb with `tsu' ending"  ,
"VERB5_U": "Godan verb with `u' ending"  ,
"VERB_5_U": "Godan verb with `u ending" ,
"VERB_SPECIAL": "Special Verb Class"  ,
"VERB_1": "Ichidan verb"  ,
"VERB_1_ZURU": "Ichidan verb - zuru verb (alternative form of -jiru verbs)"  ,
"VERB_2_RU": "Nidan verb (lower class) with `ru' ending (archaic)"  ,
"VERB_4_KU": "Yodan verb with ~ku ending" ,
"VERB_ARCHAIC": "Archaic verb",
"VERB_4_RU": "Yodan verb with ~ru ending",  
"VERB_AUXILIARY": "Auxiliary verb"  ,
"VERB_INTRANSITIVE": "Intransitive Verb"  ,
"VERB_RU": "Irregular ru verb, plain form ends with ~ri",
"VERB_SURU": "SURU verb",
"SPECIAL": "iSpecial Class of verb"  ,
"VERB_TRANSITIVE": "Transitive Verb" }


def load_vocabulary(tense):
        filename = "conjugation_table.txt"
        vocab_filename = "./GKvocab_n2.xml"
        verb_array = []
        number = 0
        counter = 0
        level_counter = 1

        print('Processing GKVocab XML File - ')
        #Main execution code
        #load the entire JMdict_e XML File 
        print('Processing GKVocab XML File: %s - ' % vocab_filename)
        tree = metree.parse(vocab_filename)

        #get root of the XML File
        root = tree.getroot()

        #get all entries in the file
        entries_x = root.findall('vocab_entry')

        for entry_x in entries_x:
            number += 1

            #Get kanji and furigana element, kanji element may be empty
            ent_seq_set_x = entry_x.findall('ent_seq')
            kanji_set = entry_x.findall('kanji') # Kanji Element
            furigana_set = entry_x.findall('furigana') # Reading Element ( furigana )
            pos_set = entry_x.findall('pos') # Find all pos
            kanji_score = 0
            furigana_score = 0
            is_verb = 0
            for pos_x in pos_set:
                s = verb_switch.get(pos_x.text, "NOT_VERB_POS"), 
                #print(s[0])
                if s[0] != "NOT_VERB_POS": #if it's tagged as verb
                    is_verb = 1
                    verb_list = [number, ent_seq_set_x[0].text, kanji_set[0].text, furigana_set[0].text, pos_set[0].text]
                    verb_array.append(verb_list)
            if is_verb == 1 :
                print(verb_list)

        return verb_array

load_vocabulary("past_tense")
