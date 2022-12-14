from datetime import datetime
def quickSort(A, low, high): #quickSort function, it will take an array as input and return a sorted array
    if(low<high):
        pivot_loc = partition(A,low,high)
        quickSort(A,low,pivot_loc-1)
        quickSort(A,pivot_loc+1,high)
    return(A)

def partition(A,low,high):
    pivot = A[high] # here we have used last element of an array as pivot
    i=low-1
    # j=low
    for j in range(low,high):
        if(A[j]<=pivot): # compare the elements with the pivot
            i=i+1
            A[i], A[j] = A[j], A[i] # if A[j] is smaller than the pivot swap A[i] and A[j]
            # print("A={} i={} j={}".format(A,i,j))  # print statements used for debugging
    # print("!!A={} i={} pivot={}".format(A, i, pivot))
    A[i+1], A[high] = A[high], A[i+1]
    return i+1
if __name__ == "__main__":
    start = datetime.now() # it will save the current time in start variable
    ans = quickSort([10,80,30,90,40,50,70],0,len([10,80,30,90,40,50,70])-1)
    end = datetime.now() # it will save the current time in end variable
    print("Result: {}".format(ans))
    print("Time= {} miliseconds".format((end-start).microseconds/1000))  #this line is used to calculate
    #and write total execution time in milliseconds by subtracting start time from end time