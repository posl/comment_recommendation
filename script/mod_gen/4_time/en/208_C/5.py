def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(10**9+1)
    ans = [0]*N
    cnt = 0
    for i in range(N):
        if i == N-1:
            ans[i] += K
        else:
            cnt += (A[i+1]-A[i])*(i+1)
            if cnt > K:
                ans[i] += K-(cnt-(A[i+1]-A[i])*(i+1))
                cnt = K
            else:
                ans[i] += A[i+1]-A[i]
    for i in range(N):
        print(ans[i])
main()
