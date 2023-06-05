def solve(n, a):
    a.sort()
    b = a[n//2]
    return sum(abs(a[i]-b-i-1) for i in range(n))

if __name__ == '__main__':
    solve()