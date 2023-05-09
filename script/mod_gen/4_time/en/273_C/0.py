def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0]*n
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans[i] = 1
    ans[n-1] = 1
    for i in range(n-1, 0, -1):
        if a[i-1] != a[i]:
            ans[i] += ans[i-1]
    for i in range(n):
        print(n-ans[i])

if __name__ == '__main__':
    solve()