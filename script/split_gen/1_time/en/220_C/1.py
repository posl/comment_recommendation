def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    S = sum(A)
    T = 0
    for i in range(N):
        T += A[i]
        if T > X:
            print(i+1)
            return
    if S <= 0:
        print(-1)
        return
    K = (X - T) // S
    T += K * S
    for i in range(N):
        T += A[i]
        if T > X:
            print(K * N + i + 1)
            return
