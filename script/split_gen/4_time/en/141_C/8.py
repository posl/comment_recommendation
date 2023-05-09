def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    A = [K - Q + 1 for _ in range(N)]
    for i in range(Q):
        A[A_i - 1] += 1
    for i in range(N):
        if A[i] > 0:
            print("Yes")
        else:
            print("No")
