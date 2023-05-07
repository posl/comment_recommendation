def solve(n, x, y, a):
    for i in range(n):
        for j in range(i+1, n):
            if (a[j]-a[i])*(y-x) == (j-i)*(a[i]+a[j]):
                return True
    return False
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
print('Yes' if solve(n, x, y, a) else 'No')

if __name__ == '__main__':
    solve()