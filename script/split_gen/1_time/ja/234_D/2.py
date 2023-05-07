def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    K -= 1
    for i in range(K, N):
        P.sort()
        print(P[K])
        P.pop(0)
