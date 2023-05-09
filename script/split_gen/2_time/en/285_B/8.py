def countLengthOfLongestNonMatchingSubstring(s):
    maxLen = 0
    for i in range(1, len(s)):
        j = 0
        while (i+j) < len(s) and s[j] != s[i+j]:
            j += 1
        if j > maxLen:
            maxLen = j
    return maxLen
