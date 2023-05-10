def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    cnt = [0] * N
    for i in range(Q):
        cnt[L[i] - 1] += 1
    for i in range(N):
        if K - Q + cnt[i] > 0:
            print("Yes")
        else:
            print("No")
