def maxSum(a):
    n = len(a)
    if n == 1:
        return a[0]
    elif n == 2:
        return max(a[0], a[1])
    else:
        if a[0] > a[1]:
            a[1] = a[0]
        for i in range(2, n):
            if a[i-1] > a[i]:
                a[i] = a[i-1]
        return a[n-1]
n = int(input())
b = list(map(int, input().split()))
a = [0] * n
for i in range(n-1):
    a[i] = b[i]
a[n-1] = b[n-2]
print(maxSum(a))
