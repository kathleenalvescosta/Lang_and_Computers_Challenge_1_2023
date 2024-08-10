#imports the necessary modules
import glob
import re

tab = '\t'
#shows the paths for both folders that will be iterated through
summary_path = "PC_7_out_file"
summary_path2 = "PC_7_out_file_2"
#for each file in the first path
for file in glob.glob(summary_path):
    #creates a file called "PC_overall_spoken_freqs"
    out_file = re.sub("PC_7_out_file", "PC_7_overall_spoken_freqs", file)
    out_file = open(out_file, 'w+')
    #writes in the following information into the file
    out_file.write('Folder Name' + tab + 'POS - Verb Raw Frequency' + tab + 'POS - Verbs per 100 words' + tab +
                   'TAG - Determiner Raw Frequency' + tab + 'TAG - Determiners per 100 words' + tab +
                   'Non-Stop Words - Raw Frequency' + tab + 'Non-Stop Words - Per 100 Words' + '\n')
    #opens each file as "file in"
    with open(file, encoding='utf-8', errors='ignore') as file_in:
        #reads in each file
        text = file_in.read()
        #creates a dictionary for the verb raw freq, determiner raw freq, nonstop raw freq, and overall word count
        values_dict = {"Verb Raw Freq": [], "Determiner Raw Freq": [], "Non-stop Raw Freq": [], "Overall Word Count": []}
        #splits each value in the file by a line break
        values = text.split("\n")
        #the zeroeth value will be appended to the verb raw freq key
        values_dict["Verb Raw Freq"].append(int(values[0]))
        #the first value will be appended to the determiner raw key
        values_dict["Determiner Raw Freq"].append(int(values[1]))
        #the second value will be appended to the nonstop raw key
        values_dict["Non-stop Raw Freq"].append(int(values[2]))
        #the third value will be appended to the overall word count key
        values_dict["Overall Word Count"].append(int(values[3]))


    #initializes a dictionary to store the sums of the different values
    sums_dict = {"Verb Raw Freq": 0, "Determiner Raw Freq": 0, "Non-stop Raw Freq": 0, "Overall Word Count": 0}

    #loops through the length of the verb raw freq key
    for i in range(len(values_dict["Verb Raw Freq"])):
        #the verb raw freq will add each of the following values in the verb raw freq values
        sums_dict["Verb Raw Freq"] += values_dict["Verb Raw Freq"][i]
        #the det raw freq will add each of the following values in the det raw freq values
        sums_dict["Determiner Raw Freq"] += values_dict["Determiner Raw Freq"][i]
        #the nonstop raw freq will add each of the following values in the nonstop raw freq values
        sums_dict["Non-Stop Raw Freq"] += values_dict["Non-stop Raw Freq"][i]
        #the overall word count will add each value of the overall word count values
        sums_dict["Overall Word Count"] += values_dict["Overall Word Count"][i]
    #these statements print each of the frequencies
    print(sums_dict["Verb Raw Freq"])
    print(sums_dict["Determiner Raw Freq"])
    print(sums_dict["Non-stop Raw Freq"])
    print(sums_dict["Overall Word Count"])

    #rewrites "sums_dict" to reflect the verb normed frequency
    sums_dict["Verb Freq per 100"] = sums_dict["Verb Raw Freq"] / sums_dict["Overall Word Count"] * 100
    # rewrites "sums_dict" to reflect the determiner normed frequency
    sums_dict["Determiner Freq per 100"] = sums_dict["Determiner Raw Freq"] / sums_dict["Overall Word Count"] * 100
    # rewrites "sums_dict" to reflect the nonstop normed frequency
    sums_dict["Non-Stop Freq per 100"] = sums_dict["Non-Stop Raw Freq"] / sums_dict["Overall Word Count"] * 100
    #writes the information that was calculated into the out_file file
    out_file.write(str(summary_path) + tab + str(sums_dict["Verb Raw Freq"].values()) + tab + str(sums_dict["Verb Freq per 100"].values() +
                tab + str(sums_dict["Determiner Raw Freq"].values()) + tab + str(sums_dict["Determiner Freq per 100"].values()) + tab +
                str(sums_dict["Non-stop Raw Freq"].values()) + tab + str(sums_dict["Non-Stop Freq per 100"]) + "\n"))
#######################################################################################################################
#for each file in "summary_path2"
for file in glob.glob(summary_path2):
    #creates a new folder called "PC_7_overall_written_freqs"
    out_file2 = re.sub("PC_7_out_file_2", "PC_7_overall_written_freqs", file)
    out_file2 = open(out_file2, 'w+')
    #writes out the information into the new file
    out_file2.write('Folder Name' + tab + 'POS - Verb Raw Frequency' + tab + 'POS - Verbs per 100 words' + tab +
                   'TAG - Determiner Raw Frequency' + tab + 'TAG - Determiners per 100 words' + tab +
                   'Non-Stop Words - Raw Frequency' + tab + 'Non-Stop Words - Per 100 Words' + '\n')
    #opens each file as file_in
    with open(file, encoding='utf-8', errors='ignore') as file_in:
        #reads in the file
        text = file_in.read()
        # creates a dictionary for the verb raw freq, determiner raw freq, nonstop raw freq, and overall word count
        values_dict = {"Verb Raw Freq": [], "Determiner Raw Freq": [], "Non-stop Raw Freq": [],
                       "Overall Word Count": []}
        # splits each value in the file by a line break
        values = text.split("\n")
        # the zeroeth value will be appended to the verb raw freq key
        values_dict["Verb Raw Freq"].append(int(values[0]))
        # the first value will be appended to the determiner raw key
        values_dict["Determiner Raw Freq"].append(int(values[1]))
        # the second value will be appended to the nonstop raw key
        values_dict["Non-stop Raw Freq"].append(int(values[2]))
        # the third value will be appended to the overall word count key
        values_dict["Overall Word Count"].append(int(values[3]))

        # initializes a dictionary to store the sums of the different values
    sums_dict = {"Verb Raw Freq": 0, "Determiner Raw Freq": 0, "Non-stop Raw Freq": 0, "Overall Word Count": 0}

    # loops through the length of the verb raw freq key
    for i in range(len(values_dict["Verb Raw Freq"])):
        # the verb raw freq will add each of the following values in the verb raw freq values
        sums_dict["Verb Raw Freq"] += values_dict["Verb Raw Freq"][i]
        # the det raw freq will add each of the following values in the det raw freq values
        sums_dict["Determiner Raw Freq"] += values_dict["Determiner Raw Freq"][i]
        # the nonstop raw freq will add each of the following values in the nonstop raw freq values
        sums_dict["Non-Stop Raw Freq"] += values_dict["Non-stop Raw Freq"][i]
        # the overall word count will add each value of the overall word count values
        sums_dict["Overall Word Count"] += values_dict["Overall Word Count"][i]
    # these statements print each of the frequencies
    print(sums_dict["Verb Raw Freq"])
    print(sums_dict["Determiner Raw Freq"])
    print(sums_dict["Non-stop Raw Freq"])
    print(sums_dict["Overall Word Count"])

    # rewrites "sums_dict" to reflect the verb normed frequency
    sums_dict["Verb Freq per 100"] = sums_dict["Verb Raw Freq"] / sums_dict["Overall Word Count"] * 100
    # rewrites "sums_dict" to reflect the determiner normed frequency
    sums_dict["Determiner Freq per 100"] = sums_dict["Determiner Raw Freq"] / sums_dict["Overall Word Count"] * 100
    # rewrites "sums_dict" to reflect the nonstop normed frequency
    sums_dict["Non-Stop Freq per 100"] = sums_dict["Non-Stop Raw Freq"] / sums_dict["Overall Word Count"] * 100
    # writes the information that was calculated into the out_file file
    out_file.write(str(summary_path) + tab + str(sums_dict["Verb Raw Freq"].values()) + tab + str(
        sums_dict["Verb Freq per 100"].values() +
        tab + str(sums_dict["Determiner Raw Freq"].values()) + tab + str(
            sums_dict["Determiner Freq per 100"].values()) + tab +
        str(sums_dict["Non-stop Raw Freq"].values()) + tab + str(sums_dict["Non-Stop Freq per 100"]) + "\n"))