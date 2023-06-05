def solve(n, arr):
    arr.sort()
    b = arr[n//2]
    ans = 0
    for i in range(n):
        ans += abs(arr[i] - (b+i+1))
    return ans
