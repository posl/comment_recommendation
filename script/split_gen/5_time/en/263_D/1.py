def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] > R:
            A[i] = R
        elif A[i] < L:
            A[i] = L
    print(sum(A))
