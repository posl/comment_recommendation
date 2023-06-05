def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[2], reverse=True)
    P.sort(key=lambda x: x[1], reverse=True)
    P.sort(key=lambda x: x[0], reverse=True)
    P_4 = [p[0] for p in P]
    P_4.sort(reverse=True)
    # print(P_4)
    for p in P:
        if p[0] >= P_4[K-1]:
            print('Yes')
        else:
            print('No')
