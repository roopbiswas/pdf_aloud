from gtts import gTTS
import os

text = "A DIZZYING ARRAY OF INTERNET END SYSTEMS. Not too long ago, the end-system devices connected to the Internet were primarily traditional computers such as desktop machines and powerful servers."
file = open("draft.txt","r").read().replace("\n"," ")
language = 'en'

speech = gTTS(str(file), lang=language, slow=False)
speech.save("text.mp3")
os.system("vlc text.mp3")
os.system("TASKKILL vlc")