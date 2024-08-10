#imports the regular expression module
import re
#initializes the variable "contraction_paragraph" as the paragraph shown
contraction_paragraph = "The monkey wasn’t happy to see the banana fall into the water. Debra hasn’t seen the movie " \
                        "about the giant mountain, but she’ll see it tonight. Debra's movie tastes aren’t like mine. " \
                        "The cat doesn’t like Jackie's new cat food. I’ll go to the market and buy sugar for the cake " \
                        "I’m planning to back for mum. During the holidays, I’ll show the circus manager the house. " \
                        "The boy wishes he’d known about the rain last night. I don’t like honey in my tea but I’ll put" \
                        "in a bit of sugar. I like saving money because it’s a good idea. The swamp won’t be too muddy" \
                        "to cross at this time of the year. The man in the shop shouldn’t be taking the picture. The" \
                        "book hasn’t been in the library for a long time but it’ll be back soon. She’s going to the " \
                        "mall. He’s got a lot to do. He’s intelligent. Bob’s interested in graduate school."
#establishes the variable "contraction_counter" and sets its value to 0
contraction_count = 0
#initializes the variable "con_words" as a list by splitting the variable "contraction_paragraph"
con_words = contraction_paragraph.split()
#initializes a for loop which will search through each element in the list "con_words"
for word in con_words:
    #searches for the characters "n't" within a word in the list
    if re.search("n’t", word):
        #if the condition of the previous line of code is found, 1 is added to the contraction counter
        contraction_count += 1
        #prints the word found in this condition
        print(word)
    #searches for the characters "'d" within a word in the list
    elif re.search("’d", word):
        # if the condition of the previous line of code is found, 1 is added to the contraction counter
        contraction_count += 1
        # prints the word found in this condition
        print(word)
    #searches for the characters "'ll'" within a word in the list
    elif re.search("’ll", word):
        # if the condition of the previous line of code is found, 1 is added to the contraction counter
        contraction_count += 1
        # prints the word found in this condition
        print(word)
    #searches for the characters "'s" within a word in the list
    elif re.search("’s", word):
        # if the condition of the previous line of code is found, 1 is added to the contraction counter
        contraction_count += 1
        # prints the word found in this condition
        print(word)
    #searches for the characters "'m" within a word in the list
    elif re.search("’m", word):
        # if the condition of the previous line of code is found, 1 is added to the contraction counter
        contraction_count += 1
        # prints the word found in this condition
        print(word)
#this calculation finds the average by dividing the number in the contraction counter by the length of the list
contraction_average = contraction_count / len(con_words)
#this calculation finds the average per 100 words by multiplying the average previously found by 100
contraction_average_per_100 = contraction_average * 100
#this prints the original paragraph
print(contraction_paragraph)
#this notifies the user of how many words are contractions per 100 words based off the paragraph
print("There is an average of " + str(round(contraction_average_per_100, 2)) + " contractions per 100 words in this "
                                                                               "paragraph.\n")
#######################################################################################################################
#initializes the variable "passive_paragraph" as the paragraph shown
passive_paragraph = "These awards, called Oscars, are presented in a formal ceremony in Hollywood. Several people are" \
                    "nominated in specific categories, such as Best Movie, Best Actor, Best Music, and Best Costumes." \
                    "One nominee is chosen to receive an award in each category. When the awards ceremony started in" \
                    "1929, 15 awards were presented and the ceremony was attended by only 250 people. Tickets cost $10," \
                    "and anyone who could afford a ticket could attend. Today about two dozen Oscars are presented." \
                    "Tickets are no longer sold to the general public; invitations are sent only to people involved in" \
                    "making the movies and to their guests. Today the awards are presented in the 3400-seat Kodak" \
                    "Theatre in Hollywood. Until 1941, the winners’ names were already known before the ceremony and" \
                    "published in newspapers the night before the ceremony. Now the winners’ names are placed in sealed" \
                    "envelopes and the envelopes are not opened until the night of the ceremony. Since 1953, Oscar night" \
                    "has been televised and broadcast all over the world. This show is seen by hundreds of millions of" \
                    "people. Viewers watch as their favorite movie stars arrive looking beautiful and hopeful."
#this line sets the value of the variable "passive_count" to 0
passive_count = 0
#this list establishes the auxiliary verb list which will be used in this paragraph
aux_verbs_list = ["are", "was", "is", "were", "been"]
#initializes the variable "passive_words" by splitting the paragraph above into a list
passive_words = passive_paragraph.split()
#this for loop looks for the words in the enumerated function of the variable "passive_words)
for index, word in enumerate(passive_words):
    #this if statement sets the index to one less of the length, so that the program does not have an error as it
    #attempts to enumerate characters which are not there (at the end of the list)
    if index < len(passive_words) - 1:
        #this if statement searches for the word in the list "aux_verb_list"
        if word in aux_verbs_list:
            #this searches for the suffix -en/-ed within the word after words identified in the aux_verb_list
            if re.search('(ed|en)$', passive_words[index + 1]):
                #if this condition is true, 1 is added to the variable "passive_count"
                passive_count += 1
                # prints the word found in this condition as well as the word that comes after it
                print(word + ' ' + passive_words[index + 1])
#this calculation finds the average by dividing the number in the contraction counter by the length of the list
passive_average = passive_count / len(passive_words)
#this calculation finds the average per 100 words by multiplying the average previously found by 100
passive_average_per_100 = passive_average * 100
#this prints the original paragraph
print(passive_paragraph)
#this notifies the user of how many words are contractions per 100 words based off the paragraph
print("There is an average of  " + str(round(passive_average_per_100, 2)) + " instances of passive voice per 100 words "
                                                                            "in this paragraph.\n")
########################################################################################################################
#initializes the variable "phrasal_paragraph" as the paragraph shown
phrasal_paragraph = "Little Johnny hated going to see the dentist. It wasn't that his dentist was nasty; it was that " \
                    "Johnny wasn't too fond of sweets. His dentist had warned him that his teeth would fall out if he " \
                    "kept up eating candy. Time and time again, the dentist had told him to cut out sweet food or at " \
                    "least cut down on the amount he ate. As he lay down in the dentist's chair, all the horrible " \
                    "memories from his last visit came back to him. On that occasion, the dentist had to pull out one " \
                    "of his teeth! The pain was terrible - even with the anesthetic the dentist had given him. When the " \
                    "anesthetic wore off it was difficult for him to eat or chew anything at all. This time the check up " \
                    "was much better. His dentist checked out his teeth, made him wash out his mouth with pink liquid " \
                    "and then told him to spit it out into the sink.  That was it. No problems and no pain! Johnny was " \
                    "delighted and so was his dentist. Johnny has finally learned his lesson and was taking better care " \
                    "of his teeth. Well done, Johnny!"
#this line sets the value of the variable "phrasal_count" to 0
phrasal_count = 0
#initializes the variable "phrasal_words" by splitting the paragraph above into a list
phrasal_words = phrasal_paragraph.split()
#this for loop looks for the words in the enumerated function of the variable "phrasal_words)
for index, word in enumerate(phrasal_words):
    # this if statement sets the index to one less of the length, so that the program does not have an error as it
    # attempts to enumerate characters which are not there (at the end of the list)
    if index < len(phrasal_words) - 1:
        #this if conditional provides a condition which the program will search for
        if word in phrasal_words:
            #if the word "down" is found after a word in the "phrasal_words" list:
            if re.search("down", phrasal_words[index + 1]):
                #then 1 will be added to the phrasal_count
                phrasal_count += 1
                # prints the word found in this condition as well as the word that comes after it
                print(word + ' ' + phrasal_words[index + 1])
            #if the previous condition is not found, the program will search for the word "out" after a word found in
            #the phrasal_words list
            elif re.search("out", phrasal_words[index + 1]):
                # then 1 will be added to the phrasal_count
                phrasal_count += 1
                # prints the word found in this condition as well as the word that comes after it
                print(word + ' ' + phrasal_words[index + 1])
             # if the previous condition is not found, the program will search for the word "up" after a word found in
             # the phrasal_words list
            elif re.search("up", phrasal_words[index + 1]):
                # then 1 will be added to the phrasal_count
                phrasal_count += 1
                # prints the word found in this condition as well as the word that comes after it
                print(word + ' ' + phrasal_words[index + 1])
            # if the previous condition is not found, the program will search for the word "back" after a word found in
            # the phrasal_words list
            elif re.search("back", phrasal_words[index + 1]):
                # then 1 will be added to the phrasal_count
                phrasal_count += 1
                # prints the word found in this condition as well as the word that comes after it
                print(word + ' ' + phrasal_words[index + 1])
            # if the previous condition is not found, the program will search for the word "off" after a word found in
            # the phrasal_words list
            elif re.search("off", phrasal_words[index + 1]):
                # then 1 will be added to the phrasal_count
                phrasal_count += 1
                # prints the word found in this condition as well as the word that comes after it
                print(word + ' ' + phrasal_words[index + 1])
#this calculation finds the average by dividing the number in the contraction counter by the length of the list
phrasal_average = phrasal_count / len(phrasal_words)
#this calculation finds the average per 100 words by multiplying the average previously found by 100
phrasal_average_per_100 = phrasal_average * 100
#this prints the original paragraph
print(phrasal_paragraph)
#this notifies the user of how many words are contractions per 100 words based off the paragraph
print("There is an average of " + (str(round(phrasal_average_per_100, 2))) + " instances of phrasal verbs per 100 words "
                                                                             "in this paragraph.\n")