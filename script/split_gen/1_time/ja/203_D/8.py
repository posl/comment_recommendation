def get_median_index(arr):
    arr.sort()
    return int((len(arr) / 2) + 1) - 1
n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans = 10 ** 9
for i in range(n - k + 1):
    for j in range(n - k + 1):
        tmp = []
        for l in range(k):
            for m in range(k):
                tmp.append(a[i + l][j + m])
        ans = min(ans, tmp[get_median_index(tmp)])
print(ans)
