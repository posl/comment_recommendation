def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    res = ['Yes' for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if P[j][0] + P[j][1] + P[j][2] > P[i][0] + P[i][1] + P[i][2]:
                res[i] = 'No'
                break
    for i in range(N):
        for j in range(i):
            if P[j][0] + P[j][1] > P[i][0] + P[i][1]:
                res[i] = 'No'
                break
    for i in range(N):
        for j in range(i):
            if P[j][0] > P[i][0]:
                res[i] = 'No'
                break
    print('\n'.join(res))
