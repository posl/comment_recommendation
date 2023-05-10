def solve():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n-1):
        for j in range(i+1, n):
            total += a[i]*a[j]
    print(total % (10**9+7))

if __name__ == '__main__':
    solve()