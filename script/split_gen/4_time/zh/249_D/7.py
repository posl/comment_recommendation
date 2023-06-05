def solve(n, arr):
    # Write your code here
    ans = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if arr[i] * arr[j] == arr[k]:
                    ans += 1
    return ans
n = int(input())
arr = list(map(int, input().split()))
print(solve(n, arr))
