#imports regex module
import re

# the raw data filepath (This is a tab-delimited text file: F4_DL_subcorpus_PC4.txt.
file_raw = 'F4_DL_subcorpus_PC4.txt'
#initializes file1 under the name "BnkrHll_quest_1"
file1 = "BnkrHll_quest_1"
#this creates the aformentioned file
out_file = open(file1 + ".txt", "w+")

#this will separate each of the columns
tab = '\t'
#this will separate each of the rows using a line break
sep = '\n'

#this opens the .txt file
with open(file_raw, encoding='utf8', errors='ignore') as file_in:
    #the .txt file is read in
    text = file_in.read()
    #removes any quotation marks using re.sub
    text = re.sub('"', '', text)
#splits the lines by using a line break
lines = text.split(sep)
#initializes a list for all the lines
line_list = []
#initializes a list for all the unique speakers in this unique quest
bunker_speakers = []
#this for loop establishes which cells will be the quest, dialogue, and speakers within the lines specified. this gives
# us our data
for line in lines[1:69]:
    cell = line.split(tab)
    quest = cell[0]
    dialogue = cell[4]
    speaker = cell[5]
    #if the speaker in this loop is not in the bunker_speakers list, it will be added to the list
    if speaker not in bunker_speakers:
        bunker_speakers.append(speaker)
    #initializes a new variable, which will add "<>" around the speaker
    file_line = "<" + speaker + ">: " + dialogue
    #this overwrites the previous line_list variable, and creates new data which has the "<>"
    line_list.append(file_line)

#writes "<quest>" into the .txt file that is created
out_file.write("<" + quest + ">" + sep)
#writes "<Number of Speakers: ...>" into the .txt file that is created
out_file.write("<Number of Speakers: " + str(len(bunker_speakers)) + ">" + sep * 2)
#this for loop will print each line, separated by a linebreak
for line in line_list:
    out_file.write(line + sep)
#######################################################################################################################
#initializes file1 under the name "Cdswrth_quest_2"
file2 = "Cdswrth_quest_2"
#this creates the aformentioned file
out_file = open(file2 + ".txt", "w+")
#initializes the list which will contain the unique speakers for this unique quest
codsworth_speakers = []
#initializes the list for the lines of dialogue in this quest
line2_list = []
#this for loop establishes which cells will be the quest, dialogue, and speakers within the lines specified.
for line in lines[70:241]:
    cell = line.split(tab)
    quest = cell[0]
    dialogue = cell[4]
    speaker = cell[5]
    #if the speaker is not found in the codsworth_speakers list, it will be appended to the list
    if speaker not in codsworth_speakers:
        codsworth_speakers.append(speaker)
    # initializes a new variable, which will add "<>" around the speaker
    file2_line = "<" + speaker + ">: " + dialogue
    # this overwrites the previous line2_list variable, and creates new data which has the "<>"
    line2_list.append(file2_line)

#writes "<quest> into the .txt file
out_file.write("<" + quest + ">" + sep)
#writes "<Number of Speakers: ..." into the .txt file
out_file.write("<Number of Speakers: " + str(len(codsworth_speakers)) + ">" + sep * 2)
#this for loop will write each line, separated by a linebreak
for line in line2_list:
    out_file.write(line + sep)
#######################################################################################################################
#initializes file3 under the name "Cncrd_quest_3"
file3 = "Cncrd_quest_3"
#this creates the aformentioned file
out_file = open(file3 + ".txt", "w+")
#initializes the list concord_speakers
concord_speakers = []
#initializes the list for the lines of dialogue in this quest
line3_list = []
#this for loop establishes which cells will be the quest, dialogue, and speakers within the lines specified.
for line in lines[242:252]:
    cell = line.split(tab)
    quest = cell[0]
    dialogue = cell[4]
    speaker = cell[5]
    # if the speaker is not found in the concord_speakers list, it will be appended to the list
    if speaker not in concord_speakers:
        concord_speakers.append(speaker)
    # initializes a new variable, which will add "<>" around the speaker
    file3_line = "<" + speaker + ">: " + dialogue
    # this overwrites the previous line3_list variable, and creates new data which has the "<>"
    line3_list.append(file3_line)

#writes "<quest>" into the .txt file that is created
out_file.write("<" + quest + ">" + sep)
#writes "<Number of Speakers: ...>" into the .txt file that is created
out_file.write("<Number of Speakers: " + str(len(concord_speakers)) + ">" + sep * 2)
#this for loop will write each line, separated by a linebreak
for line in line3_list:
    out_file.write(line + sep)
#######################################################################################################################
#initializes file4 under the name "DVlt111_quest_4"
file4 = "DVlt111_quest_4"
#this creates the aformentioned file
out_file = open(file4 + ".txt", "w+")
#initializes the list vault_speakers
vault_speakers = []
#initializes the list for the lines of dialogue in this quest
line4_list = []
#this for loop establishes which cells will be the quest, dialogue, and speakers within the lines specified.
for line in lines[253:271]:
    cell = line.split(tab)
    quest = cell[0]
    dialogue = cell[4]
    speaker = cell[5]
    # if the speaker is not found in the vault_speakers list, it will be appended to the list
    if speaker not in vault_speakers:
        vault_speakers.append(speaker)
    # initializes a new variable, which will add "<>" around the speaker
    file4_line = "<" + speaker + ">: " + dialogue
    # this overwrites the previous line4_list variable, and creates new data which has the "<>"
    line4_list.append(file4_line)

#writes "<quest>" into the .txt file that is created
out_file.write("<" + quest + ">" + sep)
#writes "<Number of Speakers: ...>" into the .txt file that is created
out_file.write("<Number of Speakers: " + str(len(vault_speakers)) + ">" + sep * 2)
#this for loop will write each line, separated by a linebreak
for line in line4_list:
    out_file.write(line + sep)
#######################################################################################################################
#initializes file5 under the name "DiMQ104_quest_5"
file5 = "DiMQ104_quest_5"
#this creates the aformentioned file
out_file = open(file5 + ".txt", "w+")
#initializes the list mq_speakers
mq_speakers = []
#initializes the list for the lines of dialogue in this quest
line5_list = []
#this for loop establishes which cells will be the quest, dialogue, and speakers within the lines specified.
for line in lines[272:304]:
    cell = line.split(tab)
    quest = cell[0]
    dialogue = cell[4]
    speaker = cell[5]
    # if the speaker is not found in the mq_speakers list, it will be appended to the list
    if speaker not in mq_speakers:
        mq_speakers.append(speaker)
    # initializes a new variable, which will add "<>" around the speaker
    file5_line = "<" + speaker + ">: " + dialogue
    # this overwrites the previous line5_list variable, and creates new data which has the "<>"
    line5_list.append(file5_line)

#writes "<quest>" into the .txt file that is created
out_file.write("<" + quest + ">" + sep)
#writes "<Number of Speakers: ...>" into the .txt file that is created
out_file.write("<Number of Speakers: " + str(len(mq_speakers)) + ">" + sep * 2)
#this for loop will write each line, separated by a linebreak
for line in line5_list:
    out_file.write(line + sep)
#######################################################################################################################
#initializes file6 under the name "DiaMS07_quest_6"
file6 = "DiaMS107_quest_6"
#this creates the aformentioned file
out_file = open(file6 + ".txt", "w+")
#initializes the list ms_speakers
ms_speakers = []
#initializes the list for the lines of dialogue in this quest
line6_list = []
#this for loop establishes which cells will be the quest, dialogue, and speakers within the lines specified.
for line in lines[305:318]:
    cell = line.split(tab)
    quest = cell[0]
    dialogue = cell[4]
    speaker = cell[5]
    # if the speaker is not found in the ms_speakers list, it will be appended to the list
    if speaker not in ms_speakers:
        ms_speakers.append(speaker)
    # initializes a new variable, which will add "<>" around the speaker
    file6_line = "<" + speaker + ">: " + dialogue
    # this overwrites the previous line6_list variable, and creates new data which has the "<>"
    line6_list.append(file6_line)

#writes "<quest>" into the .txt file that is created
out_file.write("<" + quest + ">" + sep)
#writes "<Number of Speakers: ...>" into the .txt file that is created
out_file.write("<Number of Speakers: " + str(len(ms_speakers)) + ">" + sep * 2)
#this for loop will write each line, separated by a linebreak
for line in line6_list:
    out_file.write(line + sep)
#######################################################################################################################
#initializes file7 under the name "DiMS07a_quest_7"
file7 = "DiMS07a_quest_7"
#opens the aformentioned .txt file
out_file = open(file7 + ".txt", "w+")
#initializes the list msa_speakers
msa_speakers = []
#initializes the list line7_list for all the lines in this quest
line7_list = []
#this for loop establishes which cells will be the quest, dialogue, and speakers within the lines specified.
for line in lines[319:499]:
    cell = line.split(tab)
    quest = cell[0]
    dialogue = cell[4]
    speaker = cell[5]
    # if the speaker is not found in the msa_speakers list, it will be appended to the list
    if speaker not in msa_speakers:
        msa_speakers.append(speaker)
    # initializes a new variable, which will add "<>" around the speaker
    file7_line = "<" + speaker + ">: " + dialogue
    # this overwrites the previous line7_list variable, and creates new data which has the "<>"
    line7_list.append(file7_line)

#writes "<quest>" into the .txt file that is created
out_file.write("<" + quest + ">" + sep)
#writes "<Number of Speakers: ...>" into the .txt file that is created
out_file.write("<Number of Speakers: " + str(len(msa_speakers)) + ">" + sep * 2)
#this for loop will write each line, separated by a linebreak
for line in line7_list:
    out_file.write(line + sep)









