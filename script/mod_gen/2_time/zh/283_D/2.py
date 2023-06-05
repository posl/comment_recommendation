def solve():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != '0':
            ans += 1
    if s[-1] != '0':
        print(ans)
    else:
        print(ans-1)

if __name__ == '__main__':
    solve()