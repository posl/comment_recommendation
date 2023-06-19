def solve(n, x, y, a):
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(i-j) == abs(a[i]-a[j]):
                return 'Yes'
    return 'No'
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, x, y, a))
