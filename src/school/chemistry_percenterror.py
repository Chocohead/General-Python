# Created by Eli Foster.
# Version: 0.3

import sys

x="leave"
y="stay"

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

def perform():
    calculate()
    question()

def question():
    q = input("To quit, type \'leave\', if not, type \'stay\'\n")
    print("Note that the single quotes are required, because Python is kind of stupid")
    if q==x:
        print("Fine. I'll go change my relationship status and cry now.\n")
        sys.exit()
    if q==y:
        print("I love you too.")
        perform()

perform()
'''
== CHANGELOG ==
=== 0.3 ===
* Fixed looping.
=== 0.2 ===
* Added option to choose whether you want to stay in the program or not.
* Changed pre-calculation text, and added a new line
* Cleaned up code a bit

=== 0.1 ===
* Initial build
'''
