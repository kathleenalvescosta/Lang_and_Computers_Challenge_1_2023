#import regex module
import re

#initializes the variable "noun" and prompts the user to assign it a value
noun = input("Enter a noun.\n")

#if the variable "noun" ends in the suffix "-tion":
if re.match("\w+tion$", noun):
    #tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ment":
elif re.match("\w+ment$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ness":
elif re.match ("\w+ness$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ing":
elif re.match ("\w+ing$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ous":
elif re.match("\w+ous$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-able":
elif re.match("\w+able$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ity":
elif re.match("\w+ity$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ion":
elif re.match("\w+ion$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ive":
elif re.match("\w+ive$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ful":
elif re.match("\w+ful$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-al":
elif re.match("\w+al$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " + noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ed":
elif re.match("\w+ed$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if the variable "noun" ends in the suffix "-ism":
elif re.match("\w+ism$", noun):
    # tell the user that variable noun is a nominalization
    print("I think " +noun + " is a nominalization")

#if none of the prior conditions apply:
else:
    print("I don't think " + noun + " is a nominalization.")