def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(1, n):
        if a[i-1] * a[i] < 0:
            if a[i-1] < 0:
                sum += -a[i-1]
                a[i-1] = 0
            else:
                sum += a[i]
                a[i] = 0
    if a[n-1] < 0:
        sum += -a[n-1]
        a[n-1] = 0
    else:
        sum += a[n-1]
        a[n-1] = 0
    print(sum)
