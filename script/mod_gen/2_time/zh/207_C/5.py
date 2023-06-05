def solve(a,b,c,d):
    if a <= b * d:
        return -1
    else:
        return (a + b - 1) // b

if __name__ == '__main__':
    solve()