def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0 for i in range(n)]
    for i in range(n):
        b[i] = a[i] - i
    b.sort()
    b = b[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b + i))
    print(ans)

if __name__ == '__main__':
    solve()