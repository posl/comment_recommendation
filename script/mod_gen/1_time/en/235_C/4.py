def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*Q
    K = [0]*Q
    for i in range(Q):
        X[i], K[i] = map(int, input().split())
    ans = [0]*Q
    for i in range(N):
        for j in range(Q):
            if A[i] == X[j]:
                K[j] -= 1
                if K[j] == 0:
                    ans[j] = i+1
    for i in range(Q):
        if ans[i] == 0:
            ans[i] = -1
    for i in range(Q):
        print(ans[i])

if __name__ == '__main__':
    solve()