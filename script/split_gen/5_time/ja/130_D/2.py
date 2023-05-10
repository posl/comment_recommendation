def count_subarray(arr, n, k):
    start = 0
    end = 0
    count = 0
    while end < n:
        while end < n and arr[end] <= k:
            end += 1
        count += (end - start) * (end - start + 1) // 2
        start = end + 1
        end += 1
    return count
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = count_subarray(a, n, k)
print(ans)
