from datetime import datetime
def mergeSort(a):
    # print("Inside mergeSort",a)
    n=len(a)
    if(n==1):
        return a
    l1 = mergeSort(a[:(n//2)]) # Sort the elements in the left subarray
    l2 = mergeSort(a[(n//2):])  # Sort the elements in the right subarray
    return merge(a,l1,l2)    # merge left and right subarray

def merge(a,l1,l2):
    # print("Inside merge")
    # print(l1)    # print statements used for debugging
    # print(l2)
    n1=len(l1)  # Calculate the lengths of subarrays
    n2=len(l2)
    # print(n1+n2)
    l=l1
    r=l2
    l.append(float('inf'))   # Append last element as infinity
    r.append(float('inf'))
    i=0
    j=0
    for k in range(n1+n2):
        if(l[i]<=r[j]):             # compare the element from left array with right array
            a[k]=l[i]               # save the smallest element to the main array a
            i=i+1
        else:
            a[k]=r[j]
            j=j+1
    # print("a=",a)
    return a
if __name__ == "__main__":
    start = datetime.now()
    ans=mergeSort([1,2,3,4,5,6,7,8,9]) #  sample code to run the merge sort using the given array
    end = datetime.now()
    print("Result: {}".format(ans))
    print("Time taken to sort= {time} in millisecs".format(time=((end - start).microseconds / 1000)))
