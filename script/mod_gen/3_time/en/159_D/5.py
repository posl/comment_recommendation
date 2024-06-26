def solve():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N + 1)
    for i in range(N):
        count[A[i]] += 1
    total = sum([count[i] * (count[i] - 1) // 2 for i in range(1, N + 1)])
    for i in range(N):
        print(total - (count[A[i]] - 1))

if __name__ == '__main__':
    solve()