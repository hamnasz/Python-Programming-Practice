#python practice programs 
def swapList(newlist):
    size = len(newlist)
#swap
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size -1] = temp
    return newlist
#drive code
newlist = [1, 2, 3, 4, 5]
print (swapList(newlist))