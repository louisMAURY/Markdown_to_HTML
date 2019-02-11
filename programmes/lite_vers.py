import sys
from argparse import *
from analysis import *

parser = ArgumentParser(description="select directory")
parser.add_argument("--input-directory" , "-i" , metavar = "" , help = "select an input folder")
parser.add_argument("--output-directory" , "-o" , metavar = "" , help ="select an output folder")

args = parser.parse_args()
print(args)

folder_md = args.input_directory
folder_html = args.output_directory


if folder_md:
    fiche = folder_md
    readeuh(fiche)
    a_title()
    a_list()
    a_italic_bold()
    a_link()
