def main():
    N, M, Q = map(int, input().split())
    trains = [[0 for i in range(N+1)] for j in range(M+1)]
    for i in range(M):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            trains[i][j] = 1
    for i in range(Q):
        p, q = map(int, input().split())
        count = 0
        for j in range(p, q+1):
            for k in range(M):
                if trains[k][j] == 1:
                    count += 1
                    break
        print(count)
