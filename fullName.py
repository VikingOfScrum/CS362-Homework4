def compoundName(a, b):

    fullName = a + ' ' + b

    if len(a) <= 0 or len(b) <= 0:
        return -1
    else:
        return fullName



#print("The name is", compoundName("That", "Guy"))
#print("The name is", compoundName("", "Guy"))
#print("The name is", compoundName("That", ""))