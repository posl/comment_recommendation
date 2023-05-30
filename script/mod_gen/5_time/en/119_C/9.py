def getMinMP(numBamboos, lengths, targetLengths):
    minMP = float('inf')
    for i in range(2**numBamboos):
        temp = i
        mp = 0
        lengthsCopy = lengths.copy()
        for j in range(numBamboos):
            if temp%2 == 1:
                mp += 10
                lengthsCopy[j] = 0
            temp = temp//2
        if targetLengths[0] in lengthsCopy and targetLengths[1] in lengthsCopy and targetLengths[2] in lengthsCopy:
            minMP = min(minMP, mp)
    return minMP
numBamboos, targetA, targetB, targetC = map(int, input().split())
lengths = []
for i in range(numBamboos):
    lengths.append(int(input()))
targetLengths = [targetA, targetB, targetC]
print(getMinMP(numBamboos, lengths, targetLengths))
