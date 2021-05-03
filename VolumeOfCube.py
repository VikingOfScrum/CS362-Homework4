#Volume of cube = a^3
def findVolume(a):
    volume = a*a*a
    if volume < 0:
        return -1
    else:
        return volume


#print("volume of cube is ", findVolume(3))
#print("volume of cube is ", findVolume(-6))