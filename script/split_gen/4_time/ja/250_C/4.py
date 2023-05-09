def main():
    N, Q = map(int, input().split())
    A = list(range(1, N + 1))
    for _ in range(Q):
        x = int(input())
        index = A.index(x)
        A[index], A[index - 1] = A[index - 1], A[index]
    print(*A)
