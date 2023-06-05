def problems105_d():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N):
        if i==0:
            B[i] = A[i]%M
        else:
            B[i] = (B[i-1]+A[i])%M
    B.sort()
    B.append(0)
    ans = 0
    cnt = 1
    for i in range(N):
        if B[i]==B[i+1]:
            cnt += 1
        else:
            ans += cnt*(cnt-1)//2
            cnt = 1
    print(ans)
problems105_d()
