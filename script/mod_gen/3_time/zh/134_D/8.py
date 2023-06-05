def solve():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N, 0, -1):
        s = 0
        for j in range(i, N + 1, i):
            s += b[j - 1]
        if s % 2 != a[i - 1]:
            b[i - 1] = 1
    M = sum(b)
    print(M)
    if M > 0:
        print(*[i + 1 for i in range(N) if b[i] == 1])

if __name__ == '__main__':
    solve()