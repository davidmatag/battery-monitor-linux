#!/usr/bin/env python3.6

import time

import battery as battery


while True:
    # Evaluates the condition of the battery and notify if necessary
    battery.check_status()
    # Sleep certain amount of seconds depending of the current battery level
    time.sleep(battery.get_sleep_time())
