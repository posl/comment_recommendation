def getBottoms(s):
    bottoms = 0
    v = 0
    w = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v += 1
        elif s[i] == 'w':
            w += 1
        if v > w:
            bottoms += 1
    return bottoms
S = input()
print(getBottoms(S))

if __name__ == '__main__':
    getBottoms()