# Created by Eli Foster

import random
import time
import sys
import gc

yes = 0
no = 1

def loop():
    lo = input("Would you like to roll again? (0 for yes, 1 for no)\n")
    while True:
        if lo == yes:
            run()
        elif lo == no:
            print("Program stopping...")
            time.sleep(0.4)
            gc.collect()
            sys.exit()

def run():
    number = input("How many sides would you like your dice to have? ")

    print("Number of sides recorded as " + str(number))

    time.sleep(0.3)
    print("Rolling...")
    time.sleep(1)

    new_number = random.uniform(1, number)

    print int(new_number)

    loop()

run()