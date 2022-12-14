import random
# generate following 4 input files with given number of sets of 3 randomly generated integers from 0 to 99.
numberOfInputsSets = [20,100,1000,4000]
noElemetsInSet=3
for set in numberOfInputsSets:
    file = open("./arr_{set}.txt".format(set=set),'w+')
    for i in range(set):
        nums = random.sample(range(0,99),3)
        nums.append(sum(nums))
        file.write(str(" ".join(str(n) for n in nums))+"\n")
    file.close()