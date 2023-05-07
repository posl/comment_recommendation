def main():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.append([T, T])
    now = 0
    for i in range(M+1):
        N = N - (AB[i][0] - now)
        if N <= 0:
            print('No')
            exit()
        now = AB[i][0]
        N = N + (AB[i][1] - AB[i][0])
        if N >= N:
            N = N
        else:
            N = N
    print('Yes')
