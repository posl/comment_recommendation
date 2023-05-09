def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    P_total = [sum(P[i]) for i in range(N)]
    P_total.sort(reverse=True)
    print('Yes' if P_total[K-1] == P_total[K] else 'No')
