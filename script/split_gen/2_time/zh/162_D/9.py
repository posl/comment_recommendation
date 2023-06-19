def solve():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for d in range(1, n):
            j = i + d
            k = j + d
            if k >= n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)
solve()
