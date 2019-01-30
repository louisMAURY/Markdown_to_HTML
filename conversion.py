def a_title():
    with open("markdown.md" , "r") as markdown:
        contents = markdown.readlines()
        for element in contents:
            counter = 0
            for cara in element:
                if cara == "#":
                    counter += 1

            # Title level 1
            if counter == 1:
                #h1()
                print("TITRE DE NIV 1")

            # Title level 2
            elif counter == 2:
                #h2()
                print("TITRE DE NIV 2")

            # Title level 3    
            elif counter == 3:
                #h3()
                print("TITRE DE NIV 3")

            # Title level 4
            elif counter == 4:
                #h4()
                print("TITRE DE NIV 4")

            # Title level 5
            elif counter == 5:
                #h5()
                print("TITRE DE NIV 5")

            # Title level 6
            elif counter == 6:
                #h6()
                print("TITRE DE NIV 6")


def a_list():
    with open("markdown.md" , "r") as markdown:
        contents = markdown.readlines()
        for element in contents:
            counter = 0
            for cara in element:
                if cara =="-":
                    counter = 1
            
            # Unordered list
            if counter == 1:
                #ul_li()
                print("Y'A UNE LISTE ICI")


def a_italic_bold():
    with open("markdown.md" , "r") as markdown:
        contents = markdown.readlines()
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
                #italic()
                print("C'est un mot italique")
            
            # **Bold** word
            elif counter_star == 4:
                #bold()
                print("C'est un mot gras")
            
            # _italique_ word
            if counter_under == 2:
                #italic()
                print("Italique aussi")
            
            # __bold__ word
            elif counter_under == 4:
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
