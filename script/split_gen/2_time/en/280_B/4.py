def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    A = [0] * N
    for i in range(N):
        if i % 2 == 0:
            A[i] = S[i]
        else:
            A[i] = -S[i]
    for i in range(1, N):
        A[i] += A[i - 1]
    print(' '.join(map(str, A)))
