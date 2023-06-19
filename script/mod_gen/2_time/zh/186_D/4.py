def solve(n, a):
    # Write your code here
    a.sort()
    sum = 0
    for i in range(n):
        sum += (2*i-n+1)*a[i]
    return sum

if __name__ == '__main__':
    solve()