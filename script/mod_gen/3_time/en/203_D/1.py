def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0
N,K = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
min = 10**9+1
for i in range(N-K+1):
    for j in range(N-K+1):
        lst = []
        for k in range(K):
            for l in range(K):
                lst.append(A[i+k][j+l])
        med = median(lst)
        if med < min:
            min = med
print(int(min))
I have an array of arrays of integers, and I want to find the median of each array. This is my code:
