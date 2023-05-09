def solve(a, b, x):
    if x >= a*a*b/2:
        return 90 - 2*(a*a*b-x)/(a*a*a)
    else:
        return 2*x/(a*b*b)

if __name__ == '__main__':
    solve()