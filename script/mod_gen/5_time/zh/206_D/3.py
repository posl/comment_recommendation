def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i > 0 and a[i] == a[i - 1]:
            ans += 1
        else:
            ans += 1
    if ans % 2 == 0:
        print(ans - 1)
    else:
        print(ans)

if __name__ == '__main__':
    solve()