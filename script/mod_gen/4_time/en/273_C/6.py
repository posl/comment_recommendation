def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    prev = 0
    ans = [0] * n
    for i in range(n):
        if i == 0 or a[i] != prev:
            prev = a[i]
            ans[i] = 1
        else:
            ans[i] = ans[i-1] + 1
    for i in range(n):
        print(n - ans[-1 - i])

if __name__ == '__main__':
    solve()