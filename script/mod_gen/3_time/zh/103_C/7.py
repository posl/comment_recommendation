def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, a[i] ^ a[j])
    print(ans)

if __name__ == '__main__':
    solve()