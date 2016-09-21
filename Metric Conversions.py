def convert(ml):
    tsp = round((float(ml) * 0.20288), 2)
    return tsp


print("This program will convert milliliters to teaspoons")
teaspoons = raw_input("How many milliliters? ")
milliliters = convert(teaspoons)
print (teaspoons + " milliters is equal to " + str(milliliters) + " teaspoons")
