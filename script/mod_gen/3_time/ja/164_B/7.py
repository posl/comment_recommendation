def solve(A, B, C, D):
    while A > 0 and C > 0:
        C -= B
        if C <= 0:
            return "Yes"
        A -= D
        if A <= 0:
            return "No"

if __name__ == '__main__':
    solve()