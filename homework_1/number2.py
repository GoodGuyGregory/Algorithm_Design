
def fillList(number):
    filledList = []
    for i in range(number):
        filledList.append(i + 1)
    return filledList

def f1(fillList):
    s = 0
    i = 1
    while i <= len(fillList):
        j = 1
        while j <= len(fillList)-1:
            s = s + fillList[j-1]
            j = j + 1 
        i = 2 * i
    print("f1:" + str(s))
    
    
def f2(fillList):
    s = 0
    i = 1
    while i <= len(fillList):
        j = 1
        while j <= len(fillList):
            s = s + fillList[j-1]
            j = j + i 
        i = 2 * i
    print("f2:" + str(s))
    



def main():
    testList = fillList(10)
    
    f1(testList)
    f2(testList)
    

main()