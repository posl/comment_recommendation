def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if K <= N:
        for i in range(N):
            if i < K:
                print(1)
            else:
                print(0)
    else:
        K -= N
        div, mod = divmod(K, N)
        for i in range(N):
            if mod > i:
                print(div + 1)
            else:
                print(div)
