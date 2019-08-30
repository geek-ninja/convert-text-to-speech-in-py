from gtts import gTTS
from playsound import playsound
import os

# define variables
s = "welcome to git hub."


# initialize tts, create mp3 and play
tts = gTTS(s, 'en')
tts.save("file.mp3")
playsound('file.mp3')


#another way of playing the sound
#apt-get install mpg123
#os.system("mpg123" + file.mp3)