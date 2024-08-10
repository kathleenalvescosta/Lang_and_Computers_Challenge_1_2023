#imports the regex module
import re
# These are the texts that we will process
#Obama's files:
obama_file_1 = '2008_D1_BO.txt'
obama_file_2 = '2008_D2_BO.txt'
obama_file_3 = '2008_D3_BO.txt'
obama_file_4 = '2012_D1_BO.txt'
obama_file_5 = '2012_D2_BO.txt'
obama_file_6 = '2012_D3_BO.txt'
#Obama's opponents' files:
mccain_file_1 = '2008_D1_JM.txt'
mccain_file_2 = '2008_D2_JM.txt'
mccain_file_3 = '2008_D3_JM.txt'
romney_file_1 = '2012_D1_MR.txt'
romney_file_2 = '2012_D2_MR.txt'
romney_file_3 = '2012_D3_MR.txt'

# defines the function called "analysis" which takes a .txt file as its argument
def analysis(txt_file):
    #this list will include all the text from the files once they are appended to the list
    causative_all = []
    #this variable initiates a counter for the specified linguistic feature with a starting value of 0
    causative_counts = 0
    #this list will append all cases of the linguistic feature found in the text
    causative_found = []
    # this list will include all the text from the files once they are appended to the list
    modal_all = []
    # this variable initiates a counter for the specified linguistic feature with a starting value of 0
    modal_counts = 0
    # this list will append all cases of the linguistic feature found in the text
    modal_found = []
    # this list will include all the text from the files once they are appended to the list
    factive_all = []
    # this variable initiates a counter for the specified linguistic feature with a starting value of 0
    factive_counts = 0
    # this list will append all cases of the linguistic feature found in the text
    factive_found = []
    #each file will be opened and initialized as "file_in"
    with open(txt_file, encoding='utf-8', errors='ignore') as file_in:
        # this reads in the lines of the file
        lines = file_in.readlines()
        # this for loop removes all whitespace, numbers, and puts all the text into lower case for easy analyzing
        for line in lines:
            # puts all words into lowercase
            line = line.lower()
            # removes all whitespace from the text
            line = re.sub('[^\w\s]', '', line)
            line = re.sub('\d', '', line)
            # remove initial and trailing extra whitespace
            line = line.strip()
            # splits the words into a list
            words = line.split()
            # appends the words to each list
            causative_all.extend(words)
            modal_all.extend(words)
            factive_all.extend(words)
        #for each word in the list "causative_all"
        for word in causative_all:
            #if the word "affect" is found:
            if re.search("affect", word):
                #adds 1 to the counter
                causative_counts += 1
                #and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "allow" is found:
            elif re.search("allow", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "assist" is found:
            elif re.search("assist", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "because" is found:
            elif re.search("because", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "cause" is found:
            elif re.search("cause", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "enable" is found:
            elif re.search("enable", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "enforce" is found:
            elif re.search("enforce", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "force" is found:
            elif re.search("force", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "guarantee" is found:
            elif re.search("guarantee", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "help" is found:
            elif re.search("help", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "influence" is found:
            elif re.search("influence", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "permit" is found:
            elif re.search("permit", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "prevent" is found:
            elif re.search("prevent", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
            # if the word "require" is found:
            elif re.search("require", word):
                # adds 1 to the counter
                causative_counts += 1
                # and appends the word to the list causative_found
                causative_found.append(word)
        # this takes the count of cases of causative verbs and divides it by total number of words in the text, giving
        # the average
        causative_average = causative_counts / len(causative_all)
        # this multiplies the average cases by 100, and gives the number of cases per 100 words
        causative_per_100 = causative_average * 100
#######################################################################################################################
        for word in modal_all:
            # if the word "can" is found:
            if re.search("can", word):
                # adds 1 to the counter
                modal_counts += 1
                #and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "may" is found:
            elif re.search("may", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "shall" is found:
            elif re.search("shall", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "will" is found:
            elif re.search("will", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "could" is found:
            elif re.search("could", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "might" is found:
            elif re.search("might", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "should" is found:
            elif re.search("should", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "would" is found:
            elif re.search("would", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "must" is found:
            elif re.search("must", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "won't" is found:
            elif re.search("won't", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "couldn't" is found:
            elif re.search("couldn't", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "shouldn't" is found:
            elif re.search("shouldn't", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "wouldn't" is found:
            elif re.search("wouldn't", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # if the word "mustn't" is found:
            elif re.search("mustn't", word):
                # adds 1 to the counter
                modal_counts += 1
                # and appends the word to the list "modal_all"
                modal_found.append(word)
            # this takes the count of cases of modal verbs and divides it by total number of words in the text, giving
            # the average
            modal_average = modal_counts / len(modal_all)
            # this multiplies the average cases by 100, and gives the number of cases per 100 words
            modal_per_100 = modal_average * 100
#######################################################################################################################
        for word in factive_all:
            # if the word "actually" is found:
            if re.search("actually", word):
                # adds 1 to the counter
                factive_counts += 1
                #and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "always" is found:
            elif re.search("always", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "certainly" is found:
            elif re.search("certainly", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "definitely" is found:
            elif re.search("definitely", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "indeed" is found:
            elif re.search("indeed", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "inevitably" is found:
            elif re.search("inevitably", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "in fact" is found:
            elif re.search("in fact", word):
                #adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "never" is found:
            elif re.search("never", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "of course" is found:
            elif re.search("of course", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "obviously" is found:
            elif re.search("obviously", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "really" is found:
            elif re.search("really", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "undoubtedly" is found:
            elif re.search("undoubtedly", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "without doubt" is found:
            elif re.search("without doubt", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            # if the word "no doubt" is found:
            elif re.search("no doubt", word):
                # adds 1 to the counter
                factive_counts += 1
                # and appends the word to the list "factive_all"
                factive_found.append(word)
            #this takes the count of cases of factive verbs and divides it by total number of words in the text, giving
            #the average
            factive_average = factive_counts / len(factive_all)
            #this multiplies the average cases by 100, and gives the number of cases per 100 words
            factive_per_100 = factive_average * 100
########################################################################################################################
        #this replaces the '.txt' file in each file with '_analysis.csv' in order to create the spreadsheet
        file_out_analysis = re.sub('\.txt', '_analysis.csv', txt_file)
        #this opens and creates the .csv (if it does not already exist)
        file_out_analysis = open(file_out_analysis, 'w+')
        #writes in labels into the first cell; each comma adds a new column; after these are written into the file, it
        #skips down to the next row
        file_out_analysis.write("Linguistic Feature" + "," + "Number of Occurences" + "," + "Words in Text" + "," +
                                "Occurences per 100 Words" + "," +"Words Found Containing Linguistic Feature" "\n")
        #writes in the linguistic feature, the number of cases found, the number of words in the text, the number of
        #cases per 100 words, and all of the cases found in the list "causative_found"
        file_out_analysis.write("Frequency of causative verbs," + str(causative_counts) + "," + str(len(causative_all))
                                + "," + str(causative_per_100) + "," + str(causative_found) + '\n')
        # writes in the linguistic feature, the number of cases found, the number of words in the text, the number of
        # cases per 100 words, and all of the cases found in the list "modal_found"
        file_out_analysis.write("Frequency of modal verbs," + str(modal_counts) + "," + str(len(modal_all))
                                + "," + str(modal_per_100) + "," + str(modal_found) + '\n')
        # writes in the linguistic feature, the number of cases found, the number of words in the text, the number of
        # cases per 100 words, and all of the cases found in the list "factive_found"
        file_out_analysis.write("Frequency of factive adverbs," + str(factive_counts) + "," + str(len(factive_all))
                                + "," + str(factive_per_100) + "," + str(factive_found) + '\n')


# call the function and specify the file
analysis(obama_file_1)
analysis(obama_file_2)
analysis(obama_file_3)
analysis(obama_file_4)
analysis(obama_file_5)
analysis(obama_file_6)
analysis(mccain_file_1)
analysis(mccain_file_2)
analysis(mccain_file_3)
analysis(romney_file_1)
analysis(romney_file_2)
analysis(romney_file_3)