import time #unused [implement if needed delays, add "time.sleep(0.1)"]
from sense_hat import SenseHat
from pygame import mixer

sense = SenseHat()

#pulling audio file [works sometimes :( ]
mixer.init()
mixer.music.load('filename.mp3')  #doc > replace filename.mp3 with path of og file
mixer.music.play(-1)  #doc > infinte loop

sense.clear(0, 0, 0)

while True:
  spectrum = mixer.music.get_volume() * 255 #Bahut error deta hai, kripya change mat karna
  
  sense.clear(0, 0, 0)

  for i in range(8):
    sense.set_pixel(i, 7, (spectrum, 0, 0)) #doc > show pixels with audio spectrum
    sense.set_pixel(i, 6, (spectrum, 0, 0))
    sense.set_pixel(i, 5, (spectrum, 0, 0))
    sense.set_pixel(i, 4, (spectrum, 0, 0))
    sense.set_pixel(i, 3, (spectrum, 0, 0))
    sense.set_pixel(i, 2, (spectrum, 0, 0))
    sense.set_pixel(i, 1, (spectrum, 0, 0))
    sense.set_pixel(i, 0, (spectrum, 0, 0))
    

#bhagwan ke naame pe kaam karna, nariyal chadhaunga
