def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    for i in range(K, N):
        print(P[i - K])
