def solve():
    n = int(input())
    s = input()
    r = s.count('R')
    w = s.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    ans = min(r,w)
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
            if cnt > ans:
                break
    print(ans - cnt)
