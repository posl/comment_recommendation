def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - (i + 1)
    B.sort()
    if N % 2 == 1:
        return B[N // 2] + N // 2
    else:
        return B[N // 2 - 1] + N // 2
print(solve())

if __name__ == '__main__':
    solve()