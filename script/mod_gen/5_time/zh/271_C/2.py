def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n):
        if a[i] > res + 1:
            break
        res += a[i]
    print(res + 1)

if __name__ == '__main__':
    solve()