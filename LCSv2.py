#LCS v2
a = "OASDFJQWETPOIBVNMOEITESDK"
b = "AOPOEWJLAKQOEIROSJDHBNCXNJKWEK"
def lcsDP(a,b):
        max = [[0]*(len(a)+1)]
        for i in range(len(b)):
                max.append([0]*(len(a)+1))
                testB = b[i]
                im = i + 1
                for j in range(len(a)):
                        jm = j+1
                        testA = a[j]
                        if testA == testB:
                                max[im][jm] = max[im-1][jm-1]+ 1
                        else:
                                if max[im-1][jm] > max[i][jm-1]:
                                        max[im][jm] = max[im-1][jm]
                                else:
                                        max[im][jm] = max[im][jm-1]
        print(max)
        #populates the "table"
        length = max[len(b)][len(a)] #the bottom right corner is the length
        if length == 0:
                return "No Matches!"
        #finding the actual substring
        string = ""
        rowstart = len(a)-1
        for i in range(len(b)-1,-1,-1):
                im = i +1
                for j in range(rowstart,-1,-1):
                        breaker = False
                        jm = j+1
                        if max[im][jm] > max[im-1][jm]:
                                if max[im][jm] > max[im][jm-1]:
                                        string += a[j]
                                        rowstart = j-1
                                        breaker = True
                                        print(str(im)+" "+str(jm))
                        else:
                                break #if the row above has the same value, adding the new value did nothing,
                                         #just go up a row.
                        if breaker:
                                break
                                #no else cond necessary, the else is to keep going through j.

        string = string [::-1]
        return {"length": length, "string": string}

print(lcsDP(a,b))
