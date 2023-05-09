def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A.sort()
    #print(A)
    #print(N, M)
    if M == 0:
        print(1)
        return
    else:
        L = []
        for i in range(M+1):
            L.append(A[i+1]-A[i]-1)
        L.sort()
        #print(L)
        ans = 0
        for i in range(M+1):
            if L[i] == 0:
                continue
            else:
                ans += L[i]
        print(ans)
        return
