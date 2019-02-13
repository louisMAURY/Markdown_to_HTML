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



# The function write in HTML the title which has a level 3 title
def h3(title_lv3):

    with open("fichier.html" , "a") as htm_file:
        sorting = title_lv3
        cont = sorting.split("#")
        useless = "".join(cont)
        matter = useless.split("\n")
        matter[1] = matter[0]
        matter[0] = "<h3>"
        matter.append("</h3>")
        matter.append("\n")
        tenor = "".join(matter)
        
        htm_file.write(tenor)


# The function write in HTML the title which has a level 4 title
def h4(title_lv4):

    with open("fichier.html" , "a") as htm_file:
        sorting = title_lv4
        cont = sorting.split("#")
        useless = "".join(cont)
        matter = useless.split("\n")
        matter[1] = matter[0]
        matter[0] = "<h4>"
        matter.append("</h4>")
        matter.append("\n")
        tenor = "".join(matter)
        
        htm_file.write(tenor)


# The function write in HTML the title which has a level 5 title
def h5(title_lv5):

    with open("fichier.html" , "a") as htm_file:
        sorting = title_lv5
        cont = sorting.split("#")
        useless = "".join(cont)
        matter = useless.split("\n")
        matter[1] = matter[0]
        matter[0] = "<h5>"
        matter.append("</h5>")
        matter.append("\n")
        tenor = "".join(matter)
        
        htm_file.write(tenor)


# The function write in HTML the title which has a level 6 title
def h6(title_lv6):

    with open("fichier.html" , "a") as htm_file:
        sorting = title_lv6
        cont = sorting.split("#")
        useless = "".join(cont)
        matter = useless.split("\n")
        matter[1] = matter[0]
        matter[0] = "<h6>"
        matter.append("</h6>")
        matter.append("\n")
        tenor = "".join(matter)
        
        htm_file.write(tenor)


def italic(italic_sentence , sep):

    with open("fichier.html" , "a") as htm_file:
        sorting = italic_sentence
        cont = sorting.split(sep)
        cont[0] = "<i>"
        cont.append(cont[2])
        cont[2] = "</i>"
        matter = "".join(cont)
        
        htm_file.write(matter)


def bold(bold_sentence , sep):

    with open("fichier.html" , "a") as htm_file:
        sorting = bold_sentence
        cont = sorting.split(sep)
        cont[0] = "<strong>"
        cont.append(cont[2])
        cont[2] = "</strong>"
        matter = "".join(cont)
        
        htm_file.write(matter)

def link(connection):

    with open("fichier.html" , "a") as htm_file:
        sorting = connection
        cont_lab1 = sorting.split("[")
        useless1 = "".join(cont_lab1)
        cont_lab2 = useless1.split("]")
        useless2 = "°".join(cont_lab2)
        cont_link1 = useless2.split("(")
        useless3 = "".join(cont_link1)
        cont_link2 = useless3.split(")")
        useless4 = "".join(cont_link2)
        matter = useless4.split("°")
        label = matter[0]
        the_link = matter[1]
        form_list = ['<a href="' , the_link , '">' , label , '</a>']
        final_form = "".join(form_list)

        htm_file.write(final_form)
