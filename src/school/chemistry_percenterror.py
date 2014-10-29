# Created by Eli Foster.
# Version: 0.4

import sys
import Tkinter

x=0
y=1

print("Welcome to the Percent Error calculator\n")

def calculate():
    exp = float(input("Please input the experimental value and press enter\n"))
    if type(exp) == float:
        print("Experimental value recorded as " + str(exp) +"\n")

        the = float(input("Please input the theoretical value and press enter\n"))
        print("Theoretical value recorded as " + str(the) + "\n")

        print("This is me pretending like the computer is doing a lot of work...\n")
        print("It's not.\n")

        res1 = (exp - the)
        res2 = (res1/the)
        res3 = (res2*100)
        print("Percent error: " + str(res3))
    elif type(exp) == int:
        print "What are you even doing? Floating decimals only! No integers!"
        return
    elif type(exp) == str:
        print "What are you even doing? Floating decimals only! No strings!"
        return

    return

def perform():
    calculate()
    question()
    return

def question():
    q = input("To quit, type 0, if not, type 1\n")
    if q==x:
        print("Fine. I'll go change my relationship status and cry now.\n")
        sys.exit()
    if q==y:
        print("I love you too.")
        perform()
    return

perform()

'''
== CHANGELOG ==
=== 0.4 ===
* Changed stay to 1 and leave to 0
* Added return statements to help performance.

=== 0.3 ===
* Fixed looping.

=== 0.2 ===
* Added option to choose whether you want to stay in the program or not.
* Changed pre-calculation text, and added a new line
* Cleaned up code a bit

=== 0.1 ===
* Initial build
'''
