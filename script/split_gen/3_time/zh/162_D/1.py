def findNumOfTriplet(s):
    N = len(s)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j - i != k - j:
                    ans += 1
    return ans
