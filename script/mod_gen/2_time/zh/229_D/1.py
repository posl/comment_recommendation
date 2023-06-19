def solve():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
        elif k > 0 and (i == 0 or s[i - 1] != 'X') and (i == n - 1 or s[i + 1] != 'X'):
            ans += 1
            k -= 1
    print(ans)

if __name__ == '__main__':
    solve()