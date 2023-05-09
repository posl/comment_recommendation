def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    k = K
    if k <= N:
        for i in range(N):
            if i < k:
                print(1)
            else:
                print(0)
    else:
        k -= N
        for i in range(N):
            if i == 0:
                print(k // N + 1)
            else:
                print(k // N)
