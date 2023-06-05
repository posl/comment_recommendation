def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == n - 1 - i:
            break
        if a[i] == a[i + 1]:
            ans += 1
            while i < n - 1 and a[i] == a[i + 1]:
                i += 1
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()