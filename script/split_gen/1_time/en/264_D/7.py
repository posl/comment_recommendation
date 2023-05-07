def bubblesort(s):
    count = 0
    for i in range(len(s)):
        for j in range(len(s)-1-i):
            if s[j] > s[j+1]:
                s[j],s[j+1] = s[j+1],s[j]
                count += 1
    return count
