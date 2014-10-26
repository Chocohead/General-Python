__author__ = 'elijahfoster-wysocki'

def length():
    base = input(float("What is the base unit?\n"))
    print("What conversion?\n")
    conversion = input("Enter: kilo for meter -> kilometer, centi for meter -> centimeter, or milli for meter -> millimeter\n")

    if conversion == str("kilo"):
        print str(base * 1000)

    if conversion == str("centi"):
        print str(base * 0.01)

    if conversion == str("milli"):
        print str(base * 0.001)

    return

def perform():
    print("Welcome to the Metric Conversion Calculator.\n")
    print("What property would you like to convert?\n")
    question = input(str("Enter: length for length, volume for volume, or mass for mass\n"))
    if question == "length":
        length()





perform()