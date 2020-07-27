def sets():
    colours = {"Red", "Green", "Blue", "Red", "Green"}

    colours2 = {"Red", "Purple", "Violet", "Orange", "Brown"}

    colours |= colours2


    print(colours)

    colours.add("Grey")

    print(colours)

    colours.discard("Red")

    print(colours)

    fancyColours = ["SnowWhite","GunMetal","BurntOrange", "SnowWhite"]

    short = {colour for colour in fancyColours if(colour != "GunMetal") }

    print(short)



sets()
