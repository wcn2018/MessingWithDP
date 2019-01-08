#For every value in substring 1, find the next value of substring 2 that is equal
#ADCHAGF
#ASJAKHF

s1 = "ASDLFKJWOIEQTOERIGBSDVXCJ"
s2 = "DSFLKJWEKLJAKSGNFMLAKJQHJ"

def lcsUpperStrings(s1,s2):
    l = len(s1)
    subStrings = [""]*l
    longest = ""
    for i in range(l-1,-1,-1):
        s1Char = s1[i]
        for j in range(i,l):
            testChar = s2[j]
            if testChar == s1Char:
                matchJ = j
                if len(subStrings[matchJ]) >0:
                    subStrings[i] = testChar + subStrings[matchJ]
                else:
                    subStrings[i]+= testChar
                break
        if len(subStrings[i]) > 0:
            longest =  subStrings[i]
    print(subStrings)
    if len(longest) > 0:
        return longest
    else:
        return "No Matches!"

print(lcsUpperStrings(s1,s2))
