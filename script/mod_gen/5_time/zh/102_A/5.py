def solve(N):
    ans = 1
    while True:
        if ans % 2 == 0 and ans % N == 0:
            return ans
        ans += 1

if __name__ == '__main__':
    solve()