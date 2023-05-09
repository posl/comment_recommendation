def solve():
    N,A,B,C = map(int,input().split())
    L = [int(input()) for _ in range(N)]
    ans = 10**9
    for i in range(4**N):
        a = b = c = 0
        cost = 0
        for j in range(N):
            if (i >> j*2) & 3 == 1:
                if a == 0:
                    a = L[j]
                else:
                    a += L[j]
                cost += 10
            elif (i >> j*2) & 3 == 2:
                if b == 0:
                    b = L[j]
                else:
                    b += L[j]
                cost += 10
            elif (i >> j*2) & 3 == 3:
                if c == 0:
                    c = L[j]
                else:
                    c += L[j]
                cost += 10
        if a!=0 and b!=0 and c!=0:
            cost += abs(a-A) + abs(b-B) + abs(c-C) - 30
            ans = min(ans,cost)
    print(ans)
