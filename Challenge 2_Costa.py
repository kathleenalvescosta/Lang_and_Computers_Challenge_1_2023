#imports random module
import random
#imports regular expressions module
import re

#prompts the user for an input and stores that input
human_response = input("Ask me something, human.\n")

 #sets the user input to all lowercase
human_response = human_response.lower()
#omits the question mark from the user input (if included in the user's input)
human_res = re.sub ("\?", "", human_response)
#splits the user input into elements in a list
human_split = human_res.split()

#the positive variable replies in the affirmative and rearranges the words to make a full sentence
pos = ("Yes, "+ human_split[1] + " " + human_split[0] + " " + human_split[2] + ".")
#the negative variable replies in the negative, rearranges the words to make a full sentence, and adds "not"
neg = ("No, " + human_split[1] + " " + human_split[0] + " not " + human_split [2] + ".")

#creates a list from the positive and negative variables
ai_responses = [pos, neg]
#chooses a random response, either in the affrimative or in the negative
random_response = random.choice(ai_responses)
#prints the random response
print(random_response)
