def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    for i in range(N):
        P[i].sort(reverse=True)
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] + 1 + K * 3 > N:
            print('No')
        else:
            print('Yes')
