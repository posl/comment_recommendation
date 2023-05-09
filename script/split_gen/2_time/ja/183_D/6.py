def main():
    N, W = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort()
    count = 0
    for i in range(N):
        count += P[i][2]
        if P[i][1] != P[i+1][0]:
            count = 0
        if count > W:
            print('No')
            return
    print('Yes')
