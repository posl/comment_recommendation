def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return arr[len(arr) // 2 - 1]
    else:
        return arr[len(arr) // 2]
N = int(input())
a = list(map(int, input().split()))
m = []
for i in range(N):
    for j in range(i, N):
        m.append(median(a[i:j + 1]))
print(median(m))
