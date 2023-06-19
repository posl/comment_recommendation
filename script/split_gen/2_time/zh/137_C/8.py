def solve():
    n = int(input())
    s = [input() for i in range(n)]
    s.sort()
    ans = 0
    cnt = 0
    for i in range(1,n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans += cnt*(cnt+1)//2
            cnt = 0
    ans += cnt*(cnt+1)//2
    print(ans)
