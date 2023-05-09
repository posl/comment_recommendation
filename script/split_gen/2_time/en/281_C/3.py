def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    T = T % A_sum
    for i in range(N):
        T -= A[i]
        if T < 0:
            print(i + 1, A[i] + T)
            break
