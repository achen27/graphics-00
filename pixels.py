imagefile = open("image00.ppm","w")

imagefile.write("P3\n500 500\n255\n")

pixels = ""

for x in range(500):
    for y in range(500):
        if (x < 100):
            pixels += "255 " + "0 " + "0 "
        elif (x < 200):
            pixels += "255 " + "127 " + "0 "
        elif (x < 300):
            pixels += "255 " + "255 " + "0 "
        elif (x < 400):
            pixels += "0 " + "255 " + "0 "
        else:
            pixels += "0 " + "0 " + "255 "


imagefile.write(pixels)
imagefile.close()
