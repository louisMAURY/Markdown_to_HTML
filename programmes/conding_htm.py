# The function write in HTML the title which has a level 1 title
def h1(title_lv1):

    with open("fichier.html" , "a") as htm_file:
        sorting = title_lv1
        cont = sorting.split("#")
        useless = "".join(cont)
        matter = useless.split("\n")
        matter[1] = matter[0]
        matter[0] = "<h1>"
        matter.append("</h1>")
        matter.append("\n")
        tenor = "".join(matter)
        
        htm_file.write(tenor)


# The function write in HTML the title which has a level 2 title
def h2(title_lv2):

    with open("fichier.html" , "a") as htm_file:
        sorting = title_lv2
        cont = sorting.split("#")
        useless = "".join(cont)
        matter = useless.split("\n")
        matter[1] = matter[0]
        matter[0] = "<h2>"
        matter.append("</h2>")
        matter.append("\n")
        tenor = "".join(matter)
        
        htm_file.write(tenor)
