# Copyright 2024 Richard Kaler 

# This script is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 3 of the License, or (at
# your option) any later version.

# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

#This is a clock - a nifty one at that - which I created by flashing a formatted date by hours and minutes repeatedly through a while loop. There are a lot of cool ways that a programmer can do this ...
#My clock is simple in design and great if you have no GUI at hand. I will add more to it later. 

import datetime
import time
import os

current_time = datetime.datetime.now().strftime("%I:%M:%S %p")

# Print a string starting with the current time

def print_time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S %P")
    formatted = f"\033[1;33m\033[20m{current_time}\033[0m"
    return formatted

while True:
    os.system('clear||cls')
    print(f"start: {current_time} ")
    print("current: "+print_time())
    time.sleep(1)
