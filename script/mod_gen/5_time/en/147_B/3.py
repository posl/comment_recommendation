def solve():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            ans += 1
    print(ans)
solve()

if __name__ == '__main__':
    solve()