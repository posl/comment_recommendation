def solve(n,s):
    #print(n,s)
    cnt = 0
    for i in range(0,n):
        for j in range(i+1,n):
            k = j + (j - i)
            if k >= n:
                break
            #print(i,j,k)
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                cnt += 1
    return cnt
