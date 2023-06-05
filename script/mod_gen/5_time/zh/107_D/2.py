def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) // 2
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    for j in range(i, n):
        b.append(median(a[i:j + 1]))
print(median(b))
