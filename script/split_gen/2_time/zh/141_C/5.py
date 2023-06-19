def main():
    N, K, Q = map(int, input().split())
    A = []
    for i in range(Q):
        A.append(int(input()))
    B = [0] * N
    for i in range(Q):
        B[A[i] - 1] += 1
    for i in range(N):
        if K + B[i] - Q > 0:
            print("Yes")
        else:
            print("No")
