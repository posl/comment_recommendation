def get_ans(N,A):
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]-A[j])%200 == 0:
                ans += 1
    return ans
