#imports necessary modules
import spacy
import glob
import re
#imports the module necessary to run spaCy
nlp = spacy.load("en_core_web_sm-3.5.0")

# Windows path for both registers
in_path = 'f4_spoken_imm\\*.txt'
in_path2 = 'f4_written_lore\\*.txt'

#for each file in the first register
for file in glob.glob(in_path):
    #creates a folder called "PC_out_file"
    file_out = re.sub('f4_spoken_imm', 'PC_7_out_file', file)
    file_out = open(file_out, 'w+')
    #opens each file in the "in_path"
    with open(file, encoding='utf-8', errors='ignore') as file_in:
        #each file is read in
        text = file_in.read()
        #the word count for each file is calculated using the length of each file
        word_count = len(text)
        #empty dictionaries are created for the tokens and part of speech and tokens and tags
        pos_dict = {}
        tag_dict = {}
        #counters are created for each of the linguistic features analyzed
        verb_counter = 0
        nonstop_counter = 0
        det_counter = 0
        #this will apply the spaCy module to the text
        doc = nlp(text)
        #for each word in the text:
        for token in doc:
            #if the word is not a stop word
            if not token.is_stop:
                #add 1 to the nonstop counter
                nonstop_counter += 1
        #the nonstop raw freq is equal to the nonstop counter
        nonstop_raw_freq = nonstop_counter
        #the nonstop average is the nonstop raw frequency divided by the word count
        nonstop_avg = nonstop_raw_freq / word_count
        #the nonstop per 100 words is equal to the nonstop average multiplied by 100, and rounded to the second decimal
        nonstop_per_100 = round(nonstop_avg * 100, 2)
        #these statements print the nonstop raw freq and nonstop per 100 totals
        print("NON STOP RAW:" + str(nonstop_raw_freq) + "\n")
        print("NON STOP NORMED:" + str(nonstop_per_100) + "\n")
        #for each token in the text:
        for token in doc:
            #the pos_dict is equal to the token and the token's part of speech
            pos_dict = {token: token.pos_}
            #for the values in pos_dict:
            for value in pos_dict.values():
                #if the value is equal to "VERB"
                if value == "VERB":
                    #the verb counter goes up by 1
                    verb_counter += 1
        #the verb raw freq is equal to the verb counter
        verb_raw_freq = verb_counter
        #the verb average is equal to the verb raw freq divided by the word count
        verb_avg = verb_raw_freq / word_count
        #the verbs per 100 words is equal to the verb average multiplied by 100, and rounded to the second decimal
        verb_per_100 = round(verb_avg * 100, 2)
        #these statements print the verb raw freq and verbs per 100 words totals
        print("VERB RAW:" + str(verb_raw_freq) + "\n")
        print("VERB NORMED:" + str(verb_per_100) + "\n")
        #for each token in the text
        for token in doc:
            #the tag_dict is equal to the token as the key and the tag as the value
            tag_dict = {token: token.tag_}
            #for each tag in the tag_dict
            for value in tag_dict.values():
                #if the value is equal to "DT"
                if value == "DT":
                    #the det counter increases by one
                    det_counter += 1
        #the det raw freq is equal to the det counter
        det_raw_freq = det_counter
        #the determiner average is equal to the raw frequency divided by the word count
        det_avg = det_raw_freq / word_count
        #the determiners per 100 words is equal to the determiner average multiplied by 100, rounded to the second decimal
        det_per_100 = round(det_avg * 100, 2)
        #these statements print both the determiner raw freq and determiners per 100 words total
        print("DETERMINER RAW:" + str(det_raw_freq) + "\n")
        print("DETERMINER NORMED:" + str(det_per_100) + "\n")

        #this writes these totals into each individual file, separated by a line break so that it is easier for the
        #second script to read and add up all the total for the final raw and normed frequencies
        file_out.write(str(verb_raw_freq) + "\n" + str(det_raw_freq) + "\n" + str(nonstop_raw_freq) + "\n" +
                       str(word_count) + "\n")
#######################################################################################################################
#for each file in the second path:
for file in glob.glob(in_path2):
    #creates the folder "PC_7_out_file_2"
    file_out2 = re.sub('f4_written_lore', 'PC_7_out_file_2', file)  #
    file_out2 = open(file_out2, 'w+')  #
    #opens each file as file_in:
    with open(file, encoding='utf-8', errors='ignore') as file_in:  #
        # each file is read in
        text = file_in.read()
        # the word count for each file is calculated using the length of each file
        word_count = len(text)
        # empty dictionaries are created for the tokens and part of speech and tokens and tags
        pos_dict = {}
        tag_dict = {}
        # counters are created for each of the linguistic features analyzed
        verb_counter = 0
        nonstop_counter = 0
        det_counter = 0
        # this will apply the spaCy module to the text
        doc = nlp(text)
        # for each word in the text:
        for token in doc:
            # if the word is not a stop word
            if not token.is_stop:
                # add 1 to the nonstop counter
                nonstop_counter += 1
        # the nonstop raw freq is equal to the nonstop counter
        nonstop_raw_freq = nonstop_counter
        # the nonstop average is the nonstop raw frequency divided by the word count
        nonstop_avg = nonstop_raw_freq / word_count
        # the nonstop per 100 words is equal to the nonstop average multiplied by 100, and rounded to the second decimal
        nonstop_per_100 = round(nonstop_avg * 100, 2)
        # these statements print the nonstop raw freq and nonstop per 100 totals
        print("NON STOP RAW:" + str(nonstop_raw_freq) + "\n")
        print("NON STOP NORMED:" + str(nonstop_per_100) + "\n")
        # for each token in the text:
        for token in doc:
            # the pos_dict is equal to the token and the token's part of speech
            pos_dict = {token: token.pos_}
            # for the values in pos_dict:
            for value in pos_dict.values():
                # if the value is equal to "VERB"
                if value == "VERB":
                    # the verb counter goes up by 1
                    verb_counter += 1
        # the verb raw freq is equal to the verb counter
        verb_raw_freq = verb_counter
        # the verb average is equal to the verb raw freq divided by the word count
        verb_avg = verb_raw_freq / word_count
        # the verbs per 100 words is equal to the verb average multiplied by 100, and rounded to the second decimal
        verb_per_100 = round(verb_avg * 100, 2)
        # these statements print the verb raw freq and verbs per 100 words totals
        print("VERB RAW:" + str(verb_raw_freq) + "\n")
        print("VERB NORMED:" + str(verb_per_100) + "\n")
        # for each token in the text
        for token in doc:
            # the tag_dict is equal to the token as the key and the tag as the value
            tag_dict = {token: token.tag_}
            # for each tag in the tag_dict
            for value in tag_dict.values():
                # if the value is equal to "DT"
                if value == "DT":
                    # the det counter increases by one
                    det_counter += 1
        # the det raw freq is equal to the det counter
        det_raw_freq = det_counter
        # the determiner average is equal to the raw frequency divided by the word count
        det_avg = det_raw_freq / word_count
        # the determiners per 100 words is equal to the determiner average multiplied by 100, rounded to the second decimal
        det_per_100 = round(det_avg * 100, 2)
        # these statements print both the determiner raw freq and determiners per 100 words total
        print("DETERMINER RAW:" + str(det_raw_freq) + "\n")
        print("DETERMINER NORMED:" + str(det_per_100) + "\n")

        # this writes these totals into each individual file, separated by a line break so that it is easier for the
        # second script to read and add up all the total for the final raw and normed frequencies
        file_out2.write(str(verb_raw_freq) + "\n" + str(det_raw_freq) + "\n" + str(nonstop_raw_freq) + "\n" + str
        (word_count) + "\n")
