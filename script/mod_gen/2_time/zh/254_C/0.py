def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + a[i]
    for i in range(1, n + 1):
        if i + k <= n:
            if a[i] > a[i + k]:
                return "No"
            if a[i] == a[i + k]:
                if b[i + k - 1] - b[i] > 0:
                    return "No"
    return "Yes"

if __name__ == '__main__':
    solve()