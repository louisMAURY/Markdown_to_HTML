import sys
from argparse import *

parser = ArgumentParser(description="select directory")
parser.add_argument("--input-directory" , "-i" , metavar = "" , help = "select an input folder")
parser.add_argument("--output-directory" , "-o" , metavar = "" , help ="select an output folder")

args = parser.parse_args()
print(args)









# The fonction read...just read the file
def lire(fileuh):
    with open(fileuh , "r") as markdown:
        contents = markdown.read()
        return contents
        print(contents)
liste = sys.argv[:]
print(liste)
