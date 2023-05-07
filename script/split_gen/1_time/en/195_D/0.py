def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        available = X[:L-1] + X[R:]
        available.sort()
        available = available[::-1]
        #print(available)
        used = [False] * N
        ans = 0
        for x in available:
            max_v = 0
            max_i = -1
            for j in range(N):
                if not used[j] and W[j] <= x and V[j] > max_v:
                    max_v = V[j]
                    max_i = j
            if max_i != -1:
                used[max_i] = True
                ans += V[max_i]
        print(ans)
        
main()
