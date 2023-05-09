def main():
    N,M,Q = map(int, input().split())
    W = [0]*(N+1)
    V = [0]*(N+1)
    for i in range(1,N+1):
        W[i],V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for i in range(Q)]
    for i in range(Q):
        L,R = Query[i]
        box = X[:L-1] + X[R:]
        box.sort()
        #print(box)
        used = [False]*(N+1)
        ans = 0
        for j in range(len(box)):
            max_v = 0
            max_i = 0
            for k in range(1,N+1):
                if used[k] == False and W[k] <= box[j] and max_v < V[k]:
                    max_v = V[k]
                    max_i = k
            if max_v > 0:
                used[max_i] = True
                ans += max_v
        print(ans)
