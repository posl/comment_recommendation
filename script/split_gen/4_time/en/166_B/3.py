def main():
    # input
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    # compute
    snukes = [0]*N
    for i in range(K):
        for j in range(d[i]):
            snukes[A[i][j]-1] = 1
    # output
    print(sum(snukes))
