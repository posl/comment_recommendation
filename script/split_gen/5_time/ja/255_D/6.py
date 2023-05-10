def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    A.sort()
    A.insert(0,0)
    A.append(10**9+1)
    ans = 0
    for i in range(1, N+2):
        ans += (A[i]-A[i-1])*i
    print(ans)
    for i in range(Q):
        if X[i] >= A[-1]:
            ans += (X[i]-A[-1])*(N+1)
            A[-1] = X[i]
        else:
            for j in range(1, N+2):
                if X[i] >= A[j-1] and X[i] <= A[j]:
                    ans += (X[i]-A[j-1])*j
                    ans += (A[j]-X[i])*(N+1-j)
                    A[j] = X[i]
                    break
        print(ans)
