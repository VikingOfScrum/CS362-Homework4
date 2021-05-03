from statistics import mean

def AvgElement(list):
    if len(list) == 0:
        return -1
    elif len(list) == 1:
        small = list[0]
        return small
    else:
        return mean(list)

#Test1 = [1, 4, 6]
#Test2 = []
#Test3 = [77]
#print("the mean is ", round(AvgElement(Test1),2))
#print("the mean is ", AvgElement(Test2))
#print("the mean is ", AvgElement(Test3))
