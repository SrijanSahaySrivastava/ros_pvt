import os
import time
from sense_hat import SenseHat

sense = SenseHat()

# Set the music player command
music_player = "mpg123"

# Set the music file path
music_file = "/path/to/music.mp3"

# Set the volume control command
volume_control = "amixer set PCM --"

# Set the pitch control command
pitch_control = "pitch -s"

# Set the initial volume and pitch
volume = 50
pitch = 0

# Set the volume and pitch control intervals
volume_interval = 5
pitch_interval = 5

while True:
    # Read the accelerometer data
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    # Calculate the volume and pitch changes based on the accelerometer data
    volume_change = int(x * volume_interval)
    pitch_change = int(y * pitch_interval)

    # Update the volume and pitch
    volume += volume_change
    pitch += pitch_change

    # Constrain the volume and pitch to valid values
    volume = max(0, min(100, volume))
    pitch = max(-50, min(50, pitch))

    # Set the volume and pitch using the control commands
    os.system(volume_control + str(volume) + "%")
    os.system(pitch_control + str(pitch) + " " + music_file)

    # Play the music
    os.system(music_player + " " + music_file)

    # Wait for a short period of time before reading the accelerometer data again
    time.sleep(0.1)
