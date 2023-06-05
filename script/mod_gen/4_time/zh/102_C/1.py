def solve(n, arr):
    arr.sort()
    mid = arr[n//2]
    ans = 0
    for i in range(n):
        ans += abs(arr[i]-mid)
    return ans

if __name__ == '__main__':
    solve()