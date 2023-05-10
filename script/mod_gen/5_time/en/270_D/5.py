def problem():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(K-1,-1,-1):
        if N >= A[i]:
            ans += (N//A[i])*A[i]
            N = N%A[i]
    return ans
print(problem())

if __name__ == '__main__':
    problem()