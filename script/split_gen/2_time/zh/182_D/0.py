def max_coordinate():
    n = int(input())
    a = [int(x) for x in input().split()]
    x = 0
    max_x = 0
    for i in range(n):
        x += a[i]
        if x > max_x:
            max_x = x
    print(max_x)
max_coordinate()
