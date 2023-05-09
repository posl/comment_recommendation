def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [K for _ in range(N)]
    for i in range(Q):
        scores[A[i]-1] += 1
    for i in range(N):
        if scores[i] - Q > 0:
            print("Yes")
        else:
            print("No")
    return
