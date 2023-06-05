def solve(n, k, a):
    ans = "Yes"
    for i in range(n-k):
        if a[i] > a[i+k]:
            ans = "No"
    return ans
