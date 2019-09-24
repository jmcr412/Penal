#python2

#from penal import * #importa tudo do penal.py

#import Tkinter #nao devera ser necessario

# import the library
from appJar import gui

# create a GUI variable called app
app = gui("Programa de Penal", "800x400") # inside () specify a name and size for your GUI, when you create it

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("Penal", "Bem-vindo ao programa penal")
app.setLabelBg("Penal", "white") #a string aqui do labelBg deve ter o mesmo valor da do Label acima, neste caso, "Penal"
app.setBg("white") #cor do backgroung
app.setFont(16)



# start the GUI
app.go()
