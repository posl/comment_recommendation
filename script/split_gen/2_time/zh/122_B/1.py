def getLongestACGT(s):
    longestACGT = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if isACGT(s[i:j+1]):
                if longestACGT < (j-i+1):
                    longestACGT = (j-i+1)
    return longestACGT
