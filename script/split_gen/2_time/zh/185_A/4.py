def solution():
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] + a[1] + a[2] + a[3] >= 600:
        print(4)
    elif a[0] + a[1] + a[2] >= 500:
        print(3)
    elif a[1] + a[2] + a[3] >= 500:
        print(3)
    elif a[0] + a[1] + a[3] >= 500:
        print(3)
    elif a[0] + a[2] + a[3] >= 500:
        print(3)
    elif a[0] + a[1] >= 300:
        print(2)
    elif a[0] + a[2] >= 300:
        print(2)
    elif a[0] + a[3] >= 300:
        print(2)
    elif a[1] + a[2] >= 300:
        print(2)
    elif a[1] + a[3] >= 300:
        print(2)
    elif a[2] + a[3] >= 300:
        print(2)
    elif a[0] >= 200:
        print(1)
    elif a[1] >= 200:
        print(1)
    elif a[2] >= 200:
        print(1)
    elif a[3] >= 200:
        print(1)
    else:
        print(0)
solution()
