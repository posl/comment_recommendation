def maxRainyDays():
    S = input()
    count = 0
    maxCount = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
        else:
            count = 0
        if count > maxCount:
            maxCount = count
    return maxCount
print(maxRainyDays())

if __name__ == '__main__':
    maxRainyDays()