import re
import xml.etree.ElementTree as metree
import random

verb_switch = {
"SPECIAL": "Special Class of verb"  ,
"VERB5_U": "Godan verb with `u' ending"  ,
"VERB_1": "Ichidan verb"  ,
"VERB_1_ZURU": "Ichidan verb - zuru verb (alternative form of -jiru verbs)"  ,
"VERB_2_RU": "Nidan verb (lower class) with `ru' ending (archaic)"  ,
"VERB_4_KU": "Yodan verb with ~ku ending" ,
"VERB_4_RU": "Yodan verb with ~ru ending",  
"VERB_5_BU": "Godan verb with `bu' ending" ,
"VERB_5_GU": "Godan verb with `gu' ending" ,
"VERB_5_KU": "Godan verb with `ku' ending" ,
"VERB_5_MU": "Godan verb with `mu' ending" ,
"VERB_5_RU": "Godan verb with `ru' ending" ,
"VERB_5_SU": "Godan verb with `su' ending"  ,
"VERB_5_TSU": "Godan verb with `tsu' ending"  ,
"VERB_5_U": "Godan verb with `u ending" ,
"VERB_ARCHAIC": "Archaic verb",
"VERB_AUXILIARY": "Auxiliary verb"  ,
"VERB_INTRANSITIVE": "Intransitive Verb"  ,
"VERB_IRREGULAR": "Irregular Verb" ,
"VERB_RU": "Irregular ru verb, plain form ends with ~ri",
"VERB_SPECIAL": "Special Verb Class"  ,
"VERB_SURU": "SURU verb",
"VERB_TRANSITIVE": "Transitive Verb" }

VERB_5_U = 0
VERB5_U = 0
VERB_5_TSU = 1
VERB_5_RU = 2
VERB_5_KU = 3
VERB_5_GU = 4
VERB_5_NU = 5
VERB_5_BU = 6
VERB_5_MU = 7
VERB_5_SU = 8
VERB_5_I_ERU = 9
VERB_SURU = 10
VERB_1 = 11
VERB_1_ZURU = 12
VERB_UNKNOWN = 99

DICTIONARY_FORM = 0
POLITE_FORM = 1
NEGATIVE_FORM = 2
TE_FORM = 3
TA_FORM = 4
POTENTIAL_FORM = 5
CONDITIONAL_FORM = 6
VOLITIONAL_FORM = 7
#liu mod start
POLITE_TA_FORM = 8
POLITE_NEG_TA_FORM = 9
#liu mod end
conjugation_table = [[],[],[],[],[],[],[],[],[],[], [], [], []]
#liu mod start
#conjugation_table[VERB_5_U] = 	["う", "います", "わない", "って", "った", "える", "えば", "おう"]
#conjugation_table[VERB_5_TSU] = ["つ", "ちます", "たない", "って", "った", "てる", "てば", "とう"]
#conjugation_table[VERB_5_RU] = 	["る", "ります", "らない", "って", "った", "れる", "れば", "ろう"]
#conjugation_table[VERB_5_KU] = 	["く", "きます", "かない", "いて", "いた", "ける", "けば", "こう"]
#conjugation_table[VERB_5_GU] = 	["ぐ", "ぎます", "がない", "いで", "いだ", "げる", "げば", "ごう"]
#conjugation_table[VERB_5_NU] = 	["ぬ", "にます", "なない", "んで", "んだ", "ねる", "ねば", "のう"]
#conjugation_table[VERB_5_BU] = 	["ぶ", "びます", "ばない", "んで", "んだ", "べる", "べば", "ぼう"] 
#conjugation_table[VERB_5_MU] = 	["む", "みます", "まない", "んで", "んだ", "める", "めば", "もう"]
#conjugation_table[VERB_5_SU] = 	["す" , "します", "さない", "して", "した", "せる", "せば", "そう"]
#conjugation_table[VERB_5_I_ERU] = 	["る", "ます", "ない", "て", "た", "られる", "れば", "よう"]
#conjugation_table[VERB_SURU] = 	["する", "します", "しない", "して", "した", "できる", "すれば", "しよう"]
#conjugation_table[VERB_1] = 	["る", "ます", "ない", "て", "た", "られる", "れば", "よう"]
#conjugation_table[VERB_1_ZURU] =["ずる", "じます", "じない", "じて", "じた", "じられる", "ずれば", "じよう"]

conjugation_table[VERB_5_U] = 	["う", "います", "わない", "って", "った", "える", "えば", "おう", "いました", "いませんでした"]
conjugation_table[VERB_5_TSU] = ["つ", "ちます", "たない", "って", "った", "てる", "てば", "とう", "ちました", "ちませんでした"]
conjugation_table[VERB_5_RU] = 	["る", "ります", "らない", "って", "った", "れる", "れば", "ろう", "りました", "りませんでした"]
conjugation_table[VERB_5_KU] = 	["く", "きます", "かない", "いて", "いた", "ける", "けば", "こう", "きました", "きませんでした"]
conjugation_table[VERB_5_GU] = 	["ぐ", "ぎます", "がない", "いで", "いだ", "げる", "げば", "ごう", "ぎました", "ぎませんでした"]
conjugation_table[VERB_5_NU] = 	["ぬ", "にます", "なない", "んで", "んだ", "ねる", "ねば", "のう", "にました", "にませんでした"]
conjugation_table[VERB_5_BU] = 	["ぶ", "びます", "ばない", "んで", "んだ", "べる", "べば", "ぼう", "びました", "びませんでした"] 
conjugation_table[VERB_5_MU] = 	["む", "みます", "まない", "んで", "んだ", "める", "めば", "もう", "みました", "みませんでした"]
conjugation_table[VERB_5_SU] = 	["す", "します", "さない", "して", "した", "せる", "せば", "そう", "しました", "しませんでした"]
conjugation_table[VERB_5_I_ERU] = 	["る", "ます", "ない", "て", "た", "られる", "れば", "よう", "ました", "ませんでした"]
conjugation_table[VERB_SURU] = 	["する", "します", "しない", "して", "した", "できる", "すれば", "しよう", "しました", "しませんでした"]
conjugation_table[VERB_1] = 	["る", "ます", "ない", "て", "た", "られる", "れば", "よう", "ました", "ませんでした"]
conjugation_table[VERB_1_ZURU] =["ずる", "じます", "じない", "じて", "じた", "じられる", "ずれば", "じよう", "じました", "じませんでした"]
#liu mod end


#detect type of verb
class VerbType:
    special_v = 0
    verb5_u_v = 0
    verb_1_v = 0
    verb_1_zuru_v = 0
    verb_2_ru_v = 0
    verb_4_ku_v = 0
    verb_4_ru_v = 0
    verb_5_bu_v = 0
    verb_5_gu_v = 0
    verb_5_ku_v = 0
    verb_5_mu_v = 0
    verb_5_nu_v = 0
    verb_5_ru_v = 0
    verb_5_su_v = 0
    verb_5_tsu_v = 0
    verb_5_u_v = 0
    verb_archaic_v = 0
    verb_auxiliary_v = 0
    verb_intransitive_v = 0
    verb_irregular_v = 0
    verb_ru_v = 0
    verb_special_v = 0
    verb_suru_v = 0
    verb_transitive_v = 0
    error_in_switch_v = 0

    def print(self):
        print("Verb Detection Variables:")
        print("\tispecial_v : %s" % self.special_v)
        print("\tiverb5_u_v : %s" % self.verb5_u_v )
        print("\tiverb_1_v : %s" % self.verb_1_v )
        print("\tiverb_1_zuru_v : %s" % self.verb_1_zuru_v )
        print("\tiverb_2_ru_v : %s" % self.verb_2_ru_v )
        print("\tiverb_4_ku_v : %s" % self.verb_4_ku_v )
        print("\tiverb_4_ru_v : %s" % self.verb_4_ru_v )
        print("\tiverb_5_bu_v : %s" % self.verb_5_bu_v )
        print("\tiverb_5_gu_v : %s" % self.verb_5_gu_v )
        print("\tiverb_5_ku_v : %s" % self.verb_5_ku_v )
        print("\tiverb_5_mu_v : %s" % self.verb_5_mu_v )
        print("\tiverb_5_ru_v : %s" % self.verb_5_ru_v )
        print("\tiverb_5_su_v : %s" % self.verb_5_su_v )
        print("\tiverb_5_tsu_v : %s" % self.verb_5_tsu_v )
        print("\tiverb_5_u_v : %s" % self.verb_5_u_v )
        print("\tiverb_archaic_v : %s" % self.verb_archaic_v )
        print("\tiverb_auxiliary_v : %s" % self.verb_auxiliary_v )
        print("\tiverb_intransitive_v : %s" % self.verb_intransitive_v )
        print("\tiverb_irregular_v : %s" % self.verb_irregular_v )
        print("\tiverb_ru_v : %s" % self.verb_ru_v )
        print("\tiverb_special_v : %s" % self.verb_special_v )
        print("\tiverb_suru_v : %s" % self.verb_suru_v )
        print("\tiverb_transitive_v : %s" % self.verb_transitive_v )

    def reset(self):
        self.special_v = 0
        self.verb5_u_v = 0
        self.verb_1_v = 0
        self.verb_1_zuru_v = 0
        self.verb_2_ru_v = 0
        self.verb_4_ku_v = 0
        self.verb_4_ru_v = 0
        self.verb_5_bu_v = 0
        self.verb_5_gu_v = 0
        self.verb_5_ku_v = 0
        self.verb_5_mu_v = 0
        self.verb_5_nu_v = 0
        self.verb_5_ru_v = 0
        self.verb_5_su_v = 0
        self.verb_5_tsu_v = 0
        self.verb_5_u_v = 0
        self.verb_archaic_v = 0
        self.verb_auxiliary_v = 0
        self.verb_intransitive_v = 0
        self.verb_irregular_v = 0
        self.verb_ru_v = 0
        self.verb_special_v = 0
        self.verb_suru_v = 0
        self.verb_transitive_v = 0
        return 1

    def is_special(self):
        self.special_v = 1
        s = "special_v %s" % self.special_v 
        return s
    
    def is_verb5_u(self) : 
        self.verb5_u_v = 1
        s = "verb5_u_v : %s"%  self.verb5_u_v 
        return s
    
    def is_verb_1(self) : 
        self.verb_1_v = 1
        s = "verb_1_v %s" % self.verb_1_v
        return s
    
    def is_verb_1_zuru(self) : 
        self.verb_1_zuru_v = 1
        s = "verb_1_zuru_v : %s" % self.verb_1_zuru_v 
        return s
    
    def is_verb_2_ru(self) : 
        self.verb_2_ru_v = 1
        s = "verb_2_ru_v : %s" % self.verb_2_ru_v 
        return s
    
    def is_verb_4_ku(self) : 
        self.verb_4_ku_v = 1
        s = "verb_4_ku_v : %s" % self.verb_4_ku_v 
        return s
    
    def is_verb_4_ru(self) : 
        self.verb_4_ru_v = 1
        s = "verb_4_ru_v : %s" % self.verb_4_ru_v 
        return s
    
    def is_verb_5_bu(self) : 
        self.verb_5_bu_v = 1
        s = "verb_5_bu_v : %s" % self.verb_5_bu_v 
        return s
    
    def is_verb_5_gu(self) : 
        self.verb_5_gu_v = 1
        s = "verb_5_gu_v : %s" % self.verb_5_gu_v 
        return s
    
    def is_verb_5_ku(self) : 
        self.verb_5_ku_v = 1
        s = "verb_5_ku_v : %s" % self.verb_5_ku_v 
        return s
    
    def is_verb_5_mu(self) : 
        self.verb_5_mu_v = 1
        s = "verb_5_mu_v : %s" % self.verb_5_mu_v 
        return s
    
    def is_verb_5_ru(self) : 
        self.verb_5_ru_v = 1
        s = "verb_5_ru_v : %s" % self.verb_5_ru_v 
        return s
    
    def is_verb_5_su(self) : 
        self.verb_5_su_v = 1
        s = "verb_5_su_v : %s" % self.verb_5_su_v 
        return s
    
    def is_verb_5_tsu(self) : 
        self.verb_5_tsu_v = 1
        s = "verb_5_tsu_v : %s" % self.verb_5_tsu_v 
        return s
    
    def is_verb_5_u(self) : 
        self.verb_5_u_v = 1
        s = "verb_5_u_v : %s" % self.verb_5_u_v 
        return s
    
    def is_verb_archaic(self) : 
        self.verb_archaic_v = 1
        s = "verb_archaic_v : %s" % self.verb_archaic_v 
        return s
    
    def is_verb_auxiliary(self) : 
        self.verb_auxiliary_v = 1
        s = "verb_auxiliary_v : %s" % self.verb_auxiliary_v 
        return s
    
    def is_verb_intransitive(self) : 
        self.verb_intransitive_v = 1
        s = "verb_intransitive_v : %s" % self.verb_intransitive_v 
        return s
    
    def is_verb_irregular(self) : 
        self.verb_irregular_v = 1
        s = "verb_irregular_v : %s" % self.verb_irregular_v 
        return s
    
    def is_verb_ru(self) : 
        self.verb_ru_v = 1
        s = "verb_ru_v : %s" % self.verb_ru_v 
        return s
    
    def is_verb_special(self) : 
        self.verb_special_v = 1
        s = "verb_special_v : %s" % self.verb_special_v 
        return s
    
    def is_verb_suru(self) : 
        self.verb_suru_v = 1
        s = "verb_suru_v : %s" % self.verb_suru_v 
        return s
    
    def is_verb_transitive (self) :
        self.verb_transitive_v = 1
        s = "verb_transitive_v : %s" % self.verb_transitive_v 
        return s
    
    def error_in_switch (self) :
        self.error_in_switch_v = 1
        s = "error_in_switch_v : %s" % self.error_in_switch_v 
        return s



    def detect_verb_type(self, argument):
        if argument == "SPECIAL": 
            s = self.is_special()
        elif argument == "VERB5_U": 
            s = self.is_verb5_u()
        elif argument == "VERB_1": 
            s = self.is_verb_1() 
        elif argument == "VERB_1_ZURU": 
            s = self.is_verb_1_zuru() 
        elif argument == "VERB_2_RU": 
            s = self.is_verb_2_ru() 
        elif argument == "VERB_4_KU": 
            s = self.is_verb_4_ku() 
        elif argument == "VERB_4_RU": 
            s = self.is_verb_4_ru() 
        elif argument == "VERB_5_BU": 
            s = self.is_verb_5_bu() 
        elif argument == "VERB_5_GU": 
            s = self.is_verb_5_gu() 
        elif argument == "VERB_5_KU": 
            s = self.is_verb_5_ku() 
        elif argument == "VERB_5_MU": 
            s = self.is_verb_5_mu() 
        elif argument == "VERB_5_RU": 
            s = self.is_verb_5_ru() 
        elif argument == "VERB_5_SU": 
            s = self.is_verb_5_su() 
        elif argument == "VERB_5_TSU": 
            s = self.is_verb_5_tsu() 
        elif argument == "VERB_5_U": 
            s = self.is_verb_5_u() 
        elif argument == "VERB_ARCHAIC": 
            s = self.is_verb_archaic() 
        elif argument == "VERB_AUXILIARY": 
            s = self.is_verb_auxiliary() 
        elif argument == "VERB_INTRANSITIVE": 
            s = self.is_verb_intransitive() 
        elif argument == "VERB_IRREGULAR": 
            s = self.is_verb_irregular() 
        elif argument == "VERB_RU": 
            s = self.is_verb_ru() 
        elif argument == "VERB_SPECIAL": 
            s = self.is_special() 
        elif argument == "VERB_SURU": 
            s = self.is_verb_suru() 
        elif argument == "VERB_TRANSITIVE": 
            s = self.is_verb_transitive() 
        else :
            s = self.error_in_switch()

        return s

    def get_conjugation(self, argument):
        dict_form = argument
        polite_form = ""
        negative_form = ""
        te_form = ""
        ta_form = ""
        potential_form = ""
        conditional_form = ""
        volitional_form = ""
        #liu odd start
        polite_ta_form = ""
        polite_neg_ta_form = ""
        #liu odd end
        VERB_TYPE = VERB_UNKNOWN
        table = [dict_form]
        if self.verb_suru_v  :
            VERB_TYPE = VERB_SURU
        elif self.verb5_u_v or  self.verb_5_u_v  :
            VERB_TYPE = VERB_5_U
        elif self.verb_5_tsu_v:
            VERB_TYPE = VERB_5_TSU
        elif self.verb_5_ru_v:
            VERB_TYPE = VERB_5_RU
        elif self.verb_5_ku_v:
            VERB_TYPE = VERB_5_KU
        elif self.verb_5_gu_v:
            VERB_TYPE = VERB_5_GU
        elif self.verb_5_nu_v:
            VERB_TYPE = VERB_5_NU
        elif self.verb_5_bu_v:
            VERB_TYPE = VERB_5_BU
        elif self.verb_5_mu_v:
            VERB_TYPE = VERB_5_MU
        elif self.verb_5_su_v:
            VERB_TYPE = VERB_5_SU
        elif self.verb_1_v:
            VERB_TYPE = VERB_1
        elif self.verb_1_zuru_v:
            VERB_TYPE = VERB_1_ZURU

        if VERB_TYPE != VERB_UNKNOWN :
            polite_form = dict_form.replace(conjugation_table[VERB_TYPE][DICTIONARY_FORM], conjugation_table[VERB_TYPE][POLITE_FORM])
            negative_form = dict_form.replace(conjugation_table[VERB_TYPE][DICTIONARY_FORM], conjugation_table[VERB_TYPE][NEGATIVE_FORM])
            te_form = dict_form.replace(conjugation_table[VERB_TYPE][DICTIONARY_FORM], conjugation_table[VERB_TYPE][TE_FORM])
            ta_form = dict_form.replace(conjugation_table[VERB_TYPE][DICTIONARY_FORM], conjugation_table[VERB_TYPE][TA_FORM])
            potential_form = dict_form.replace(conjugation_table[VERB_TYPE][DICTIONARY_FORM], conjugation_table[VERB_TYPE][POTENTIAL_FORM])
            conditional_form = dict_form.replace(conjugation_table[VERB_TYPE][DICTIONARY_FORM], conjugation_table[VERB_TYPE][CONDITIONAL_FORM])
            volitional_form = dict_form.replace(conjugation_table[VERB_TYPE][DICTIONARY_FORM], conjugation_table[VERB_TYPE][VOLITIONAL_FORM])
            #liu mod start
            polite_ta_form = dict_form.replace(conjugation_table[VERB_TYPE][DICTIONARY_FORM], conjugation_table[VERB_TYPE][POLITE_TA_FORM])
            polite_neg_ta_form = dict_form.replace(conjugation_table[VERB_TYPE][DICTIONARY_FORM], conjugation_table[VERB_TYPE][POLITE_NEG_TA_FORM])
            #liu mod end

            table.append(polite_form)
            table.append(negative_form)
            table.append(te_form)
            table.append(ta_form)
            table.append(potential_form)
            table.append(conditional_form)
            table.append(volitional_form)
            #liu mod start
            table.append(polite_ta_form)
            table.append(polite_neg_ta_form)
            #liu mod end


        print("Dictionary Form : %s" % dict_form)
        print(" - Polite Form %s" % polite_form)
        print(" - Negative Form %s" % negative_form)
        print(" - Te Form %s" % te_form)
        print(" - Ta Form %s" % ta_form)
        print(" - Potential Form %s" % potential_form)
        print(" - Conditional Form %s" % conditional_form)
        print(" - Volitional Form %s" % volitional_form)
        #liu mod start
        print(" - Polite Ta Form %s" % polite_ta_form)
        print(" - Polite Neg Ta Form  %s" % polite_neg_ta_form)
        #liu mod end

        return table

def load_vocabulary(tense):

    filename = "conjugation_table.txt"
    vocab_filename = "./GKvocab_n2.xml"
    verb_filename = "./GKverbs_n2.xml"
    verb_array = []
    number = 0
    counter = 0
    level_counter = 1
    verb_xml_h = open(verb_filename,"w") #always append to file

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

        verb_type = VerbType()
        #verb_type.reset()

        # reset detection variables

        #Get kanji and furigana element, kanji element may be empty
        ent_seq_set_x = entry_x.findall('ent_seq')
        dict_seq_set_x = entry_x.findall('dict_seq')
        kanji_set = entry_x.findall('kanji') # Kanji Element
        furigana_set = entry_x.findall('furigana') # Reading Element ( furigana )
        pos_set = entry_x.findall('pos') # Find all pos
        def_set = entry_x.findall('definition') # Find all definitions
        misc_set = entry_x.findall('misc') # Find all misc
        s_inf_set = entry_x.findall('s_inf') # Find all s_inf
        kanji_score = 0
        furigana_score = 0
        is_verb = 0

        pos_list = []
        for pos_x in pos_set:
            s = verb_switch.get(pos_x.text, "NOT_VERB_POS"), 
            #print(s[0])
            if s[0] != "NOT_VERB_POS": #if it's tagged as verb
                is_verb = 1
                status = verb_type.detect_verb_type(pos_x.text) 
                pos_list.append(pos_x.text)
                #verb_type.print()

        #If it has a verb tag
        if is_verb == 1 :
            if verb_type.verb_special_v or verb_type.verb_irregular_v or verb_type.special_v:
                verb_list = ["SPECIAL", number, ent_seq_set_x[0].text, kanji_set[0].text, furigana_set[0].text, pos_list]
                #print(verb_list)
            else: 
                verb_list = ["REGULAR", number, ent_seq_set_x[0].text, kanji_set[0].text, furigana_set[0].text, pos_list]
                verb_tense_table = verb_type.get_conjugation(kanji_set[0].text)
                verb_xml_h.write("<verb_entry>\n")
                verb_xml_h.write("<ent_seq>%s</ent_seq>\n" % ent_seq_set_x[0].text)
                verb_xml_h.write("<dict_seq>%s</dict_seq>\n" % dict_seq_set_x[0].text)
                verb_xml_h.write("<kanji>%s</kanji>\n" % kanji_set[0].text)
                verb_xml_h.write("<furigana>%s</furigana>\n" % furigana_set[0].text)
                for pos_x in pos_set:
                    verb_xml_h.write("<pos>%s</pos>\n" % pos_x.text)
                for def_x in def_set:
                    verb_xml_h.write("<definition>%s</definition>\n" % def_x.text)
                for misc_x in misc_set:
                    verb_xml_h.write("<misc>%s</misc>\n" % misc_x.text)
                for s_inf_x in s_inf_set:
                    verb_xml_h.write("<s_inf>%s</s_inf>\n" % s_inf_x.text)

                verb_xml_h.write("<polite_form>%s</polite_form>\n" % verb_tense_table[1]) 
                verb_xml_h.write("<negative_form>%s</negative_form>\n" % verb_tense_table[2])
                verb_xml_h.write("<te_form>%s</te_form>\n" % verb_tense_table[3])
                verb_xml_h.write("<ta_form>%s</ta_form>\n" % verb_tense_table[4])
                verb_xml_h.write("<potential_form>%s</potential_form>\n" % verb_tense_table[5])
                verb_xml_h.write("<conditional_form>%s</conditional_form>\n" % verb_tense_table[6])
                verb_xml_h.write("<volitional_form>%s</volitional_form>\n" % verb_tense_table[7])
                #liu mod start
                verb_xml_h.write("<polite_ta_form>%s</polite_ta_form>\n" % verb_tense_table[8])
                verb_xml_h.write("<polite_neg_ta_form>%s</polite_neg_ta_form>\n" % verb_tense_table[9])
                #liu mod end
                verb_xml_h.write("</verb_entry>\n\n")



    return verb_array

load_vocabulary("past_tense")
