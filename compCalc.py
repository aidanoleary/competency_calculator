def compCalc():
    compDict = {}
    f = open('C:\Aidan\comp_calc\competencies2.txt', 'r')
    for line in f:
        for item in line.split(','):
            comp = item.strip()
            if comp in compDict:
                compDict[comp] = compDict[comp] + 1
            else:
                compDict[comp] = 1
            
    f.close()
    print("============ Placement Diary Competencies =============")
    for item in sorted(compDict):
        print(item + ": " + str(compDict[item]) + "\n")
    
