def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(N, K, A)
    def check(X):
        #print(X)
        a = 0
        for i in range(N):
            #print(a, A[i], X)
            a += (A[i] ^ X)
        #print(a)
        return a <= K
    #print(check(2))
    X = 0
    for i in range(40, -1, -1):
        if (X + (1 << i)) <= A[-1] and check(X + (1 << i)):
            X += (1 << i)
        #print(X)
    print(X + K)

if __name__ == '__main__':
    solve()