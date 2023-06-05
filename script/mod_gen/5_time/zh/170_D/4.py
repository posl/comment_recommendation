def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(10**6+1)
    ans = 0
    for i in range(n):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()