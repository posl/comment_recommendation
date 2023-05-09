def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        return max(A[0] + A[1], A[0] - A[1], -A[0] + A[1], -A[0] - A[1])
    if N == 3:
        return max(
            A[0] + A[1] + A[2],
            A[0] + A[1] - A[2],
            A[0] - A[1] + A[2],
            A[0] - A[1] - A[2],
            A[0] - A[1] - A[2],
            A[0] - A[1] - A[2],
            - A[0] + A[1] + A[2],
            - A[0] + A[1] - A[2],
            - A[0] - A[1] + A[2],
            - A[0] - A[1] - A[2],
        )
    if N % 2 == 0:
        return sum(A) + max(
            max(A),
            min(A),
            -max(A),
            -min(A),
            0
        )
    else:
        return sum(A) + max(
            max(A),
            min(A),
            -max(A),
            -min(A),
            0,
            -2 * min(A),
            -2 * max(A)
        )
print(solve())

if __name__ == '__main__':
    solve()