def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    max = 0
    for i in range(n):
        for j in range(i,n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    for i in range(n-1):
        if max < a[i+1] - a[i]:
            max = a[i+1] - a[i]
    if max < 360 - a[n-1] + a[0]:
        max = 360 - a[n-1] + a[0]
    print(360 - max)
