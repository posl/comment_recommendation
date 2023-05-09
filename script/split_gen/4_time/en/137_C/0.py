def solve():
    N = int(input())
    S = [sorted(input()) for i in range(N)]
    S.sort()
    ans = 0
    cnt = 0
    for i in range(N-1):
        if S[i]==S[i+1]:
            cnt += 1
        else:
            ans += cnt*(cnt+1)//2
            cnt = 0
    ans += cnt*(cnt+1)//2
    print(ans)
