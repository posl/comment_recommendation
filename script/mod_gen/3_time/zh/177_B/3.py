def solve():
    s = input()
    t = input()
    ans = 1000
    for i in range(len(s) - len(t) + 1):
        count = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                count += 1
        ans = min(ans, count)
    print(ans)
solve()
