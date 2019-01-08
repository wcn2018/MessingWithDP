#Longest Increasing Subsequence of one list:
a = [121,312,4,35,1346,426,34,56734,123,568,8,797689,123124,35,4364,565,758,67909,98,238,9202,220,3,75,324]
# work backwards. Check the value before it. if <, the length of LIS for that subset
# is the LIS of the subset starting in front of it
# if a[i] > a[i-1], the start checking the LIS of subsets from a[i+1] to a[len(a)]
# the LIS of a[i] is then the highest LIS from a[i+1] to a[len(a)]
# sort the list of LIS values to find the greatest, and return it.
#lines of code related to the LIS reconstructor (gives the actual LIS) are marked

def lis(a):
        #print(a)
        longestSub = [1]*len(a)
        nextVal = [[]for i in range(len(a))] #list of lists with NoneType
                                                #reconstructor
        currentLargest = a[len(a)-1]
        for i in range(len(a)-1,0,-1):
                longestFollower = 0
                if a[i-1]>currentLargest:
                        currentLargest = a[i-1]
                        longestSub[i-1] = 1
                        pass
                #print(a[i-1])
                for j in range(i,len(a)):                                
                        if a[j]>a[i-1]:
                                test = longestSub[j]
                                #print(test)
                                if test>longestFollower:
                                        longestFollower = test
                                        nextVal[i-1].append(j)# add the index of
                                        #each longestFollower (maybe multiple)
                        longestSub[i-1] = longestFollower + 1
                #print(longestSub)
        extra = longestSub
        extra.sort()
        returnLength = extra[len(a)-1]

        #the actual constructor:
        allLIS = [] #a list of all the longest integer substrings
        seed = [ind for ind in range(0,len(nextVal)) if nextVal[ind] == []]
        #^ a list of the indices in a where the starting values are
        print(seed)
        print(nextVal)
        allLIS = [[]for i in range(len(seed))]
        for i in range(len(seed)):
                currentEnd = seed[i]
                allLIS[i].append(a[currentEnd])
                for j in range(seed[i]):
                        if currentEnd in nextVal[j]:
                                print(nextVal[j])
                                currentEnd = j
                                allLIS[i].append(a[currentEnd])
                                print(allLIS)
        print("allLIS:", allLIS)
                                

        #finalLIS = [x for x in allLIS if len(x) == returnLength]

print(lis(a))
