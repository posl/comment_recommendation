def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    print('Yes' if P[K-1][0] + P[K-1][1] + P[K-1][2] > 0 else 'No')
