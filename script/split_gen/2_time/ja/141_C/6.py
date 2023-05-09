def main():
    N, K, Q = [int(x) for x in input().split()]
    A = [int(input()) for i in range(Q)]
    P = [K for i in range(N)]
    for i in range(Q):
        P[A[i]-1] += 1
    for i in range(N):
        if P[i] - Q > 0:
            print("Yes")
        else:
            print("No")
