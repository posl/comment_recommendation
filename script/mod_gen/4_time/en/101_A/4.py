def solve(S):
    ans = 0
    for s in S:
        if s == '+':
            ans += 1
        else:
            ans -= 1
    return ans
S = input()
print(solve(S))

if __name__ == '__main__':
    solve()