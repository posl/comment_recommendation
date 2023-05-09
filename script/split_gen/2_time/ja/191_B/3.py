def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] == X:
            A[i] = 0
    for i in range(N):
        if A[i] != 0:
            print(A[i], end=" ")
