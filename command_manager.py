import os
from pygame import mixer
from gtts import gTTS
import pyttsx

class CommandManager:
	
	def __init__(self):
		self.engine = pyttsx.init('sapi5')
	
	def callCommand(self,text):
		if text == 'greeting':
			self.greeting()
		elif text == 'music':
			self.music()
		elif text == 'question':
			self.question()
		else:
			self.speak('I do not understand')
			
	def greeting(self):
		self.speak('hello sir')
		
	def music(self):
		self.speak('sorry sir, i can not play music now')
		
	def question(self):
		self.speak('sorry sir, i can not answer that question')
		
	def speak(self,speech):
		self.engine.say(speech)
		self.engine.runAndWait()
		print('Spoke')