def triangle(L):
    L.sort()
    cnt = 0
    for i in range(len(L)-2):
        for j in range(i+1,len(L)-1):
            for k in range(j+1,len(L)):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    cnt += 1
    return cnt
N = int(input())
L = list(map(int,input().split()))
print(triangle(L))
