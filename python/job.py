import sys
import os
import time
from omxplayer import OMXPlayer

player = OMXPlayer('/mnt/music.mp3')
player.play()
time.sleep(20)
player.stop()
