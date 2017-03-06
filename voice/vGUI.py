#Steven Pitts
import Tkinter
from Tkinter import *
from sound.sound import Sound
from sound.audioRecorder import AudioRecorder
class VGUI:
	def __init__(self, master,infoDict):
	
		
		
		self.master = master
		self.infoDict = infoDict
		self.audioRecorder = AudioRecorder(self)
		
		master.title("Intercom")
		
		Label(master, text = "Send your message to others on the network!\n\n").pack()
		self.record_button = Button(master, text="Record Message",command=self.recordPress)
		self.record_button.pack()
		
	
	def recordPress(self):
		wasRecording = (self.record_button["text"] == "Stop Recording") #There must be a better way of doing this
		if wasRecording:
			data = self.audioRecorder.recordAudio()
			self.sendData(data)
			self.record_button["text"] = "Record Message"
		else:
			self.record_button["text"] = "Stop Recording"
	def sendData(self, data):
		newSound = Sound(data,self.getName())
		newSound.sendData()
	def getName (self):
		return self.infoDict["firstName"]+" "+self.infoDict["lastName"]