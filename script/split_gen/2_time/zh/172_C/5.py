def solve(n,m,k,alist,blist):
    sum = 0
    i = 0
    j = 0
    while(i < n and sum + alist[i] <= k):
        sum += alist[i]
        i += 1
    ans = i
    while(j < m and i >= 0):
        sum += blist[j]
        j += 1
        while(sum > k and i > 0):
            i -= 1
            sum -= alist[i]
        if sum <= k:
            ans = max(ans,i+j)
    return ans
