def a_title():
    with open("markdown.md" , "r") as markdown:
        contents = markdown.readlines()
        for element in contents:
            compte = 0
            for cara in element:
                if cara == "#":
                    compte += 1

            # Title level 1
            if compte == 1:
                #h1()
                print("TITRE DE NIV 1")

            # Title level 2
            elif compte == 2:
                #h2()
                print("TITRE DE NIV 2")

            # Title level 3    
            elif compte == 3:
                #h3()
                print("TITRE DE NIV 3")

            # Title level 4
            elif compte == 4:
                #h4()
                print("TITRE DE NIV 4")

            # Title level 5
            elif compte == 5:
                #h5()
                print("TITRE DE NIV 5")

            # Title level 6
            elif compte == 6:
                #h6()
                print("TITRE DE NIV 6")


def a_list():
    with open("markdown.md" , "r") as markdown:
        contents = markdown.readlines()
        for element in contents:
            compteur = 0
            for cara in element:
                if cara =="-":
                    compteur = 1
            
            # Unordered list
            if compteur == 1:
                print("Y'A UNE LISTE ICI")


def a_italic_bold():
    with open("markdown.md" , "r") as markdown:
        contents = markdown.readlines()
        for elements in contents:
            compteur_star = 0
            compteur_under = 0
            for cara in elements:
                if cara == "*":
                    compteur_star += 1
                elif cara == "_":
                    compteur_under += 1
            
            # *Italique* word        
            if compteur_star == 2:
                #italic()
                print("C'est un mot italique")
            
            # **Bold** word
            elif compteur_star == 4:
                #bold()
                print("C'est un mot gras")
            
            # _italique_ word
            if compteur_under == 2:
                #italic()
                print("Italique aussi")
            
            # __bold__ word
            elif compteur_under == 4:
                #bold()
                print("Gras aussi")
            

def a_lien():
    with open("markdown.md" , "r") as markdown:
        contents = markdown.readlines()
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
                # link()
                print("C'EST UN LIIIIIIIIIIIIIIEEEEEN")



a_title()
a_list()
a_italic_bold()
a_lien()
