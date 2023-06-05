def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    sumA = [0]*(N+1)
    for i in range(N):
        sumA[i+1] = sumA[i] + A[i]
    modA = [0]*N
    for i in range(N):
        modA[i] = sumA[i+1] % M
    modA.sort()
    modA.append(-1)
    ans = 0
    c = 1
    for i in range(N):
        if modA[i] == modA[i+1]:
            c += 1
        else:
            ans += c*(c-1)//2
            c = 1
    print(ans)
solve()
