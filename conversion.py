with open("markdown.md" , "r") as markdown:
    contents = markdown.readlines()
    #print(contents)
    for element in contents:
        compte = 0
        for cara in element:
            if cara == "#":
                compte += 1
                print(compte)

                if compte == 1:
                    print("TITRE DE NIV 1")

                elif compte == 2:
                    print("TITRE DE NIV 2")
                
                elif compte == 3:
                    print("TITRE DE NIV 3")


#with open("markdown.md" , "r") as md:
#    list_lines = md.readlines()
#print(list_lines)