def solve():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = [0]
    b_sum = [0]
    for i in range(n):
        a_sum.append(a_sum[i]+a[i])
    for i in range(m):
        b_sum.append(b_sum[i]+b[i])
    ans = 0
    #print(a_sum,b_sum)
    for i in range(n+1):
        if a_sum[i] > k:
            break
        for j in range(m+1):
            if a_sum[i]+b_sum[j] > k:
                break
            if i+j > ans:
                ans = i+j
    print(ans)
