def median(arr):
    if len(arr) % 2 == 0:
        return (arr[int(len(arr)/2)] + arr[int(len(arr)/2)-1])/2
    else:
        return arr[int(len(arr)/2)]
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append(a[i])
    print(int(median(sorted(b))), end=" ")
print()
