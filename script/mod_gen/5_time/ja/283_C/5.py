def solve(s):
    ans = 0
    while s:
        if s[-1] == '0':
            s = s[:-1]
            ans += 1
        else:
            s = str(int(s) - 1)
            ans += 1
    return ans
s = input()
print(solve(s))

if __name__ == '__main__':
    solve()