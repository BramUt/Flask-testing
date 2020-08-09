import time
import numpy as np
from urllib.request import *

import sounddevice


while True:
    print(urlopen("http://192.168.2.16:5000/timediff").read().decode().rstrip())
    # time.sleep(0.5)
