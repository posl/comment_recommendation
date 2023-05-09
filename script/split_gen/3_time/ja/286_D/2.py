def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(2**N):
        sum = 0
        for j in range(N):
            if (i>>j & 1):
                sum += A[j] * B[j]
        if (sum == X):
            print("Yes")
            return
    print("No")
