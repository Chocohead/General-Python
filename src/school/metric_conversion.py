__author__ = 'elijahfoster-wysocki'

length=0
volume=1
mass=2

def length():
    base = float(input("What is the base unit?\n"))
    print("What conversion?\n")
    conversion = input("Enter: kilo for meter -> kilometer, centi for meter -> centimeter, or milli for meter -> millimeter\n")

    if conversion == str("kilo"):
        print str(base * 1000)

    if conversion == str("centi"):
        print str(base * 0.01)

    if conversion == str("milli"):
        print str(base * 0.001)

    return

def volume():
    base = float(input("What is the base unit?\n"))
    print("What conversion?\n")
    conversion = input("Enter: kilo for liter -> kiloliter, centi for liter -> centiliter, or milli for liter -> milliliter\n")

    if conversion == str("kilo"):
        print str(base * 1000)

    if conversion == str("centi"):
        print str(base * 0.01)

    if conversion == str("milli"):
        print str(base * 0.001)

    return

def mass():
    base = float(input("What is the base unit?\n"))
    print("What conversion?\n")
    conversion = input("Enter: kilo for gram -> kilogram, centi for gram -> centigram, or milli for gram -> milligram\n")

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
    question = int(input("Enter: 0 for length, 1 for volume, or 2 for mass\n"))
    if question == length:
        length()
    elif question == volume:
        volume()
    elif question == mass:
        mass()
    else:
        print("nigga.")

    return


perform()