# c'est un brouillon

# --------- IMPORTATION ------------
from tkinter import *

# ----------------------------------
# ----- DECLARATIONS BIDONS --------
fenetre = Tk()
# ----------------------------------
# -------Appel de fonction----------


# ****** menu de demmarage *********
title_sof = Label(fenetre , text = "Markdown to HTML" , font = "BurbankBigCondensed-Bold 55" , fg = "white" , bg = "#383435")
boutton_new = Button(fenetre, text = "New Markdown Document" , cursor = "hand1")
title_sof.pack()
boutton_new.pack()
# ----------------------------------
# ~~~~~~~~ LE PLUS IMPORTANT ~~~~~~~~~
fenetre.mainloop()