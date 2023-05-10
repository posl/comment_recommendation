def main():
    N,M,Q = map(int,input().split())
    train = [[0 for i in range(N)] for j in range(M)]
    for i in range(M):
        L,R = map(int,input().split())
        for j in range(L-1,R):
            train[i][j] = 1
    for i in range(Q):
        p,q = map(int,input().split())
        ans = 0
        for j in range(p-1,q):
            for k in range(M):
                if train[k][j] == 1:
                    ans += 1
        print(ans)
