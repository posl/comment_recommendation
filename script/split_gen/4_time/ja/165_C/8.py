def main():
    N, M, Q = map(int, input().split())
    A = [1] * N
    for i in range(N):
        A[i] = 1
    max = 0
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        if A[b-1] - A[a-1] == c:
            A[b-1] = d
            if max < sum(A):
                max = sum(A)
    print(max)
