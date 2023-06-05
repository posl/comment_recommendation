def d170():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if i == 0:
            if a[i] != a[i+1]:
                count += 1
        elif i == n-1:
            if a[i] != a[i-1]:
                count += 1
        elif a[i] != a[i-1] and a[i] != a[i+1]:
            count += 1
    print(count)
