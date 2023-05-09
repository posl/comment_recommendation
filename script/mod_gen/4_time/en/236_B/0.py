def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (N + 1)
    for i in range(4 * N - 1):
        cnt[A[i]] += 1
    for i in range(1, N + 1):
        if cnt[i] % 2 == 1:
            return i
print(solve())

if __name__ == '__main__':
    solve()