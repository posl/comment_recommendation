def solve(n):
    if n%2==0:
        return int(n/2)
    else:
        return int(n/2+1)

if __name__ == '__main__':
    solve()