def getStrLen(str):
    maxLen = 0
    count = 0
    for i in range(len(str)):
        if str[i] == 'A' or str[i] == 'C' or str[i] == 'G' or str[i] == 'T':
            count += 1
            if count > maxLen:
                maxLen = count
        else:
            count = 0
    return maxLen
str = input()
print(getStrLen(str))
