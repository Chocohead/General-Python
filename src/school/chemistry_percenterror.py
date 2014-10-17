# Created by Eli Foster.
# Version: 0.2-dev

import sys

quit_msg = "leave"
stay_msg = "stay"

print("Welcome to the Percent Error calculator\n")

def calculate():
    exp = float(input("Please input the experimental value and press enter\n"))
    print("Experimental value recorded as " + str(exp) +"\n")

    the = float(input("Please input the theoretical value and press enter\n"))
    print("Theoretical value recorded as " + str(the) + "\n")

    print("This is me pretending like the computer is doing a lot of work...\n")
    print("It's not.\n")

    res1 = (exp - the)
    res2 = (res1/the)
    res3 = (res2*100)
    print("Percent error: " + str(res3))

    return;

calculate();

q = input("To quit, type 'leave', if not, type 'stay'\n")
if q==quit_msg:
    print("Fine. I'll go change my relationship status and cry now.\n")
    sys.exit()
if q==stay_msg:
    print("I love you too.")
    calculate();

'''
== CHANGELOG ==
=== 0.2 ===
* Changed pre-calculation text, and added a new line
* Cleaned up code a bit
=== 0.1 ===
* Initial build
'''
