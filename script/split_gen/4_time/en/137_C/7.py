def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    C = [0]*N
    for i in range(N):
        C[i] = tuple(sorted(S[i]))
    C.sort()
    ans = 0
    cnt = 0
    for i in range(N-1):
        if C[i] == C[i+1]:
            cnt += 1
        else:
            ans += cnt*(cnt+1)//2
            cnt = 0
    ans += cnt*(cnt+1)//2
    print(ans)
