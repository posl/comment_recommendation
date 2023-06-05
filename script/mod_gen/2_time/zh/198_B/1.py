def solve(n):
    if n<3:
        return 0
    if n%2==1:
        return int((n-1)/2)
    else:
        return int((n-2)/2)

if __name__ == '__main__':
    solve()