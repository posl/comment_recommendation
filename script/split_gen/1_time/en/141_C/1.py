def main():
    # input
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    # compute
    # output
    for i in range(1, N+1):
        if K - Q + A.count(i) > 0:
            print("Yes")
        else:
            print("No")
