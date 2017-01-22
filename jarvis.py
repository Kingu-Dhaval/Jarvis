import asyncio
import websockets
import os
from pygame import mixer
from gtts import gTTS
from tempfile import TemporaryFile
import sys
import webbrowser


def speak(speech):
	mixer.init()
	mixer.music.load('hello.mp3')
	tts = gTTS(text=speech, lang='en')
	tts.save("tmp.mp3")
	
	mixer.music.load('tmp.mp3')
	mixer.music.play()
	
	print('Spoke')

def main():
	
	os.chdir('D:Python/Kings')
	webbrowser.open('http://localhost/jarvis/jarvis.php')
	async def hello(websocket, path):
	
		#Listen ----------
		msg = await websocket.recv()
		print("< {}".format(msg))
		
		# THINK HERE ----------------------------------------------
		#------
		#------
		
		#React
		if msg == " close" or msg == "close":
			asyncio.get_event_loop().stop()
			
		#Reply
		speak(msg)
		
	start_server = websockets.serve(hello, 'localhost', 9999)
	loop=asyncio.get_event_loop()
	loop.run_until_complete(start_server)
	loop.run_forever()

if __name__ == "__main__":
	main()