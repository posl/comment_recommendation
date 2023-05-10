def solve():
    n = int(input())
    s = input()
    ans = [0] * (n + 1)
    cnt = 0
    for i in range(n):
        if s[i] == 'L':
            ans[i + 1] = i + 1
            ans[i] = i + 2
            cnt = i + 2
        else:
            ans[i + 1] = cnt
            cnt += 1
    print(*ans)
