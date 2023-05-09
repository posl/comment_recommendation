def solve():
    N = int(input())
    s = [input() for _ in range(N)]
    s.sort()
    s.append('')
    ans = 0
    cnt = 1
    for i in range(N):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    print(ans)
