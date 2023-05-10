def get_median(data):
    data.sort()
    if len(data) % 2 == 0:
        return (data[len(data)//2 - 1] + data[len(data)//2]) / 2
    else:
        return data[len(data)//2]
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i, n):
        m.append(get_median(a[i:j+1]))
print(get_median(m))
