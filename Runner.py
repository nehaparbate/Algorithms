import sys
sys.path.insert(0,'./')
from insertionSort import insertionSort
from mergesort import mergeSort
from datetime import datetime
from quicksort import quickSort

# insertionSort([90, 54, 2, 6, 1, 3, 4])
print("Select Algorithm to use(1-3)\n1.Insertion Sort\n2.Merge Sort\n3.Quick Sort\n")
algoNum = int(input())
if algoNum==1:
    algoToUse='insertion'
elif algoNum==2:
    algoToUse='merge'
elif algoNum == 3:
        algoToUse = 'quick'
else:
    print("Wrong Input")
    exit()

''' this section will read all the input files and will pass the 'sum' column to the respective sorting algorithm 
selected by user
Here hash map is used to store the input arrays
After sorting it will generate output file inside 'output' folder'''

numberOfInputsSets = [20,100,1000,4000]
# numberOfInputsSets = [20]
for nLen in numberOfInputsSets:
    hashM = {}
    f = open('./arr_{nLen}.txt'.format(nLen=nLen),'r')
    outFile = open('./output/{algoToUse}_outArr_{nLen}.txt'.format(algoToUse=algoToUse,nLen=nLen),'w+')
    for i in f:
        inputNumbers = [int(n) for n in i[:-1].split(" ")]
        if(inputNumbers[-1] not in hashM):
            hashM[inputNumbers[-1]] = [inputNumbers[:-1]]
        else:
            hashM[inputNumbers[-1]].append(inputNumbers[:-1])
    f.close()
    # print(hashM[127])
    # ?ans={}
    if(algoToUse=='insertion'):
        start = datetime.now() # it will save the current time in start variable
        sortedSum = insertionSort(list(hashM.keys()))
        end = datetime.now() # it will save the current time in end variable
    elif(algoToUse=='merge'):
        start = datetime.now() # it will save the current time in start variable
        sortedSum = mergeSort(list(hashM.keys()))
        end = datetime.now() # it will save the current time in end variable
    elif(algoToUse=='quick'):
        start = datetime.now() # it will save the current time in start variable
        sortedSum = quickSort(list(hashM.keys()),0,len(list(hashM.keys()))-1)
        end = datetime.now() # it will save the current time in end variable

    # print("sum\tn1\tn2\tn3")  # print statements used for debugging
    outFile.write(("n1\tn2\tn3\tsum\n"))
    for i in sortedSum:
        for j in range(len(hashM[i])):
            # print('{i}\t{nums}'.format(i=i,nums=hashM[i][j]))
            outFile.write(" ".join(str(n) for n in hashM[i][j])+" {i}\n".format(i=i))
    outFile.write("Sorting time: {time} milliseconds".format(time=((end - start).microseconds / 1000))) #this line is used to calculate
    #and write total execution time in milliseconds by subtracting start time from end time
    print("Sorting time for {algoToUse} algorithm for {nLen} inputs: {time} milliseconds".format(algoToUse=algoToUse,nLen=nLen,time=((end-start).microseconds/1000)))
    outFile.close()


