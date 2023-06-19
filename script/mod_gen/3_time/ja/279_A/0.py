def solve():
    s = input()
    ans = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            ans += 1
    print(ans)
solve()
