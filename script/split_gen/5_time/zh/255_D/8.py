def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    ans = []
    for i in range(Q):
        count = 0
        for j in range(N):
            if A[j] > X[i]:
                count += A[j] - X[i]
            else:
                count += X[i] - A[j]
        ans.append(count)
    for i in range(Q):
        print(ans[i])
