from conding_htm import *

fileuh = "markdown.md"
fichier = "markdown.md"
# The fonction read...just read the file
def readeuh(fileuh):
    with open(fileuh , "r") as markdown:
        global contents
        contents = markdown.readlines()
        return contents


# The function say the level of the title
def a_title():
    readeuh(fichier)
    for element in contents:
        counter = 0
        for cara in element:
            if cara == "#":
                counter += 1

        # Title level 1
        if counter == 1:
            h1(element)
            print("TITRE DE NIV 1")

        # Title level 2
        elif counter == 2:
            h2(element)
            print("TITRE DE NIV 2")

        # Title level 3    
        elif counter == 3:
            h3(element)
            print("TITRE DE NIV 3")

        # Title level 4
        elif counter == 4:
            h4(element)
            print("TITRE DE NIV 4")

        # Title level 5
        elif counter == 5:
            h5(element)
            print("TITRE DE NIV 5")

        # Title level 6
        elif counter == 6:
            h6(element)
            print("TITRE DE NIV 6")

# The function say if their is a list
def a_list():
    readeuh(fichier)
    for element in contents:
        counter = 0
        for cara in element:
            if cara =="-":
                counter = 1
            
        # Unordered list
        if counter == 1:
            #ul_li()
            print("Y'A UNE LISTE ICI")

# The function say if their is an important part text and the type of the program
def a_italic_bold():
    readeuh(fichier)
    for element in contents:
        counter_star = 0
        counter_under = 0
        for cara in element:
            if cara == "*":
                counter_star += 1
            elif cara == "_":
                counter_under += 1
            
        # *Italique* word        
        if counter_star == 2:
            italic(element , "*")
            print("C'est un mot italique")
            
        # **Bold** word
        elif counter_star == 4:
            bold(element , "**")
            print("C'est un mot gras")
            
        # _italique_ word
        if counter_under == 2:
            italic(element , "_")
            print("Italique aussi")
            
        # __bold__ word
        elif counter_under == 4:
            bold(element , "__")
            print("Gras aussi")
            
# The function say if their is a link
def a_link():
    readeuh(fichier)
    for element in contents:
        counter = 0
        for cara in element:
            if cara =="[":
                counter += 1
            if cara == "]":
                counter += 1
            if cara == "(":
                counter += 1
            if cara == ")":
                counter += 1
                
        # link
        if counter == 4:
            link(element)
            print("C'EST UN LIEN")



a_title()
a_list()
a_italic_bold()
a_link()
