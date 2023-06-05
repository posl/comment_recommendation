def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    t = [0] * N
    now = 0
    cnt = 0
    while t[now] == 0:
        t[now] = cnt
        cnt += 1
        now = A[now] - 1
    loop = cnt - t[now]
    if K < t[now]:
        now = 0
        for i in range(K):
            now = A[now] - 1
    else:
        K -= t[now]
        K %= loop
        now = 0
        for i in range(K):
            now = A[now] - 1
    print(now + 1)
