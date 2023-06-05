def solve():
    n = int(input())
    A = list(map(int, input().split()))
    res = [0] * (2 * n + 1)
    res[1] = 0
    for i in range(n):
        res[2 * i + 2] = res[A[i]] + 1
        res[2 * i + 3] = res[A[i]] + 1
    for i in range(1, 2 * n + 1):
        print(res[i])

if __name__ == '__main__':
    solve()