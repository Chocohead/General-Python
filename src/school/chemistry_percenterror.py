# Created by Eli Foster.
# Version: 0.1

print("Welcome to the Percent Error calculator\n")
exp = float(input("Please input the experimental value and press enter\n"))
print("Experimental value recorded as " + str(exp) +"\n")
the = float(input("Please input the theoretical value and press enter\n"))
print("Theoretical value recorded as " + str(the) + "\n")
print("I will now do stuff\n")

res1 = (exp - the)
res2 = (res1/the)
res3 = (res2*100)

print("Percent error: " + str(res3))
