import glob
import re

path = "F4_DL_subcorpus_PC4\\*.txt"
file_out = open("F4_spoken_data.csv", "w+")
file_out.write("QUEST, DIALOGUE LINE, SPEAKER")

for file in glob.glob(path):
    print(file)
