from datetime import datetime

def insertionSort(a):
	#print("Previous: ",a)
	for i in range(1,len(a)): # iterate the array a from 2nd position to 2nd last element of the array
		key=a[i]
		j=i-1
		while j>=0 and a[j]>key: # compare key with previous elements until the key is less
			#print("in while")
			a[j+1]=a[j] # Shift the greater values one position to the right
			j=j-1
		a[j+1]=key # store the key to the correct sorted position
		#print(a)    # print statements used for debugging
	#print(a)
	return a
if __name__ == "__main__":
	start = datetime.now()
	ans=insertionSort([90,54,2,6,1,3,4,6,3,6,4,545,453,3453]) #  sample code to run the insertion sort using the given array
	end = datetime.now()
	print("Result: {}".format(ans))
	print("Time taken to sort= {time} in milisecs".format(time=((end-start).microseconds/1000)))