import sys

def lire_ecrire():

    mark = open("markdown.md" , "r")
    contenu = mark.read()

    html = open("fichier.html" , "w")
    html.write(contenu)

    html.close()
    mark.close()

    html_lu = open("fichier.html" , "r")
    print(html_lu.read())
    html_lu.close()

# The fonction read...just read the file
def read(fileuh):
    with open(fileuh , "r") as markdown:
        contents = markdown.read()
        return contents
        print(contents)

read(sys.argv[1]) # Pour selectionner le fichier
