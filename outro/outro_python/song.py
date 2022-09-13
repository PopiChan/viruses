# import required module
import os
  
# play sound
file = "C:Users/User/Desktop/code/viruses/viruses/outro/outro_python/Outro-Music.mp3"
print('playing sound using native player')
os.system("mpg123 " + file)