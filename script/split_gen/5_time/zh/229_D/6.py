def solve():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ans += 1
    ans += 2 * k
    print(min(ans, n - 1))
