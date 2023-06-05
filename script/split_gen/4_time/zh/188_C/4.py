def getSecond(l):
    if len(l) == 2:
        if l[0][1] > l[1][1]:
            return l[1][0]
        else:
            return l[0][0]
    else:
        newl = []
        for i in range(0, len(l), 2):
            if l[i][1] > l[i+1][1]:
                newl.append(l[i])
            else:
                newl.append(l[i+1])
        return getSecond(newl)
n = int(input())
a = list(map(int, input().split()))
l = []
for i in range(len(a)):
    l.append([i+1, a[i]])
print(getSecond(l))
