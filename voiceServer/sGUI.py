#Steven Pitts
import Tkinter
from Tkinter import *
from sound.sound import Sound
class SGUI:
	def __init__(self, master,infoDict):
	
		
		
		self.master = master
		self.infoDict = infoDict
		
		master.title("Intercom Server")
		
		labelText = "The purpose of this is to recieve and echo the messages it recieves.\n\n"
		self.label = Label(master, text = labelText)
		self.label.pack()
		demoSound = Sound("This is the demo data","Steven Demo")
		self.receiveData(demoSound)
		print demoSound
	def receiveData(self, sound):
		print "Sound has been received:"
		print " ",sound