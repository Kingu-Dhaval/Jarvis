import asyncio
import websockets
import os
from pygame import mixer
from gtts import gTTS
from tempfile import TemporaryFile

def listen():
	async def hello(websocket, path):
		msg = await websocket.recv()
		print("< {}".format(msg))
		websocket.stop()
		asyncio.get_event_loop().stop()
	start_server = websockets.serve(hello, 'localhost', 9999)
	loop=asyncio.get_event_loop()
	loop.run_until_complete(start_server)
	loop.run_forever()
	
	
def speak(speech):

	os.chdir('D:Python/Kings')
	tts = gTTS(text=speech, lang='en')
	tts.save("hello.mp3")
	mixer.init()
	mixer.music.load('hello.mp3')
	mixer.music.play()
	print('Spoke')