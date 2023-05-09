def solve():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    a[1] = b[0]
    for i in range(1, n - 1):
        a[i + 1] = min(b[i], a[i])
    print(sum(a))

if __name__ == '__main__':
    solve()