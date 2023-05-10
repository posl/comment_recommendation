def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i+1, n+1):
        m.append(median(a[i:j]))
print(median(m))

if __name__ == '__main__':
    median()