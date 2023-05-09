def solve(N, A, B, C, ls):
    global ans
    if N == 0:
        if C == 0 or B == 0 or A == 0:
            return
        ans = min(ans, abs(A - a) + abs(B - b

if __name__ == '__main__':
    solve()