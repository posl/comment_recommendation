def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    s = set()
    for i in range(n):
        if a[i] in s:
            ans += 1
        else:
            s.add(a[i])
    print(ans)

if __name__ == '__main__':
    solve()