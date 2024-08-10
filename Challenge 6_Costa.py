#imports the modules for this code
import re
import glob

# the path to the directory in which all the txt files are stored
mini_core_all_texts = 'Mini-CORE\\*.txt'

# create the csv file that is written out with the frequency data
csv_file_out = open('pc6_lexical_bundle_data.csv', 'w+')
# Write the column headers in the .csv file
csv_file_out.write('lexical bundle,raw frequency,normed frequency,text rate\n')
#initializes an empty list for all the lexical bundles that will be found
all_lbs = []
#for every file in the file path "mini_core_all_texts"
for file in glob.glob(mini_core_all_texts):
    #opens each file as "file_in"
    with open(file, encoding="utf-8", errors="ignore") as file_in:
        #initializes an empty list of lexical bundles for each sentence
        lexical_bundles = []
        #sets the word_count to 0
        word_count = 0
        # Initialize a variable named text and set its value to the contents of the .txt file
        text = file_in.read()
        # remove characters enclosed in angled brackets <for example, remove these characters in angled brackets>
        text = re.sub('<.+>', '', text)
        # make all characters lower case
        text = text.lower()
        # remove characters except for letters, punctuation, and white space
        text = re.sub("[^\w\s|\\\.|\\\?|!|]|,|\n", "", text)
        # remove commas because lexical bundles can cross commas (but not sentence boundaries)
        text = re.sub(",", "", text)
        # remove extra white space at beginning and end of text
        text = text.strip()
        # store the total number of words in the text in text_word_counts_dict
        word_count = len(text.split())
        text_rate = 0
        # Initialize a list in which each item is a sentence from the text
        #splits each sentence by various different punctuation marks
        sentences = re.split("\.|;|\?|!\n", text)
        #for each sentence in the list "sentences":
        for sentence in sentences:
            #splits the sentence into each word
            words = sentence.split()
            #if the length of the list of words is greater than or equal to 4
            if len(words) >= 4:
                #for each enumerated word
                for i, word in enumerate(words):
                    #if there is more than 3 letters after the current word:
                    if i + 3 < len(words):
                        #the bundle will consist of the current word plus the next 3 words after it
                        bundles = word + " " + words[i + 1] + ' ' + words[i + 2] + ' ' + words[i + 3]
                        #appends this bundle to the "lexical_bundles" list
                        lexical_bundles.append(bundles)
        #for each bundle in lexcial_bundles:
        for bundle in set(lexical_bundles):
            #the raw freq is equal to the number of bundles in the list lexical_bundles
            raw_freq = lexical_bundles.count(bundles)
            #if the raw freq is greater than or equal to 5:
            if raw_freq >= 5:
                #if the bundle is not in all_bundles:
                if bundle not in all_lbs:
                    #bundle is added
                    all_lbs.append(bundle)
                    #and the text_rate is equal to 1
                    text_rate = 1
                #if the bundle is already in the list:
                else:
                    #1 is added to the raw freq
                    raw_freq += 1
                    #and 1 is also added to the text_rate
                    text_rate += 1
        #the normed frequency is the raw freq divided by the word count, times 100
        norm_freq = (raw_freq/word_count * 100)
    #for each lexical bundle in all_lbs:
    for lbs in all_lbs:
        #writes the bundle, raw frq, normed freq, and text rate into the csv file
        csv_file_out.write(str(lbs) + "," + str(raw_freq) + "," + str(norm_freq) + "," + str(text_rate) + '\n')
