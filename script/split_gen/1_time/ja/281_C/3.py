def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    time = sum(A)
    T %= time
    for i in range(N):
        if T - A[i] <= 0:
            print(i+1, T)
            break
        T -= A[i]
