def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] + a[2] + a[3] >= 300:
        print(4)
    elif a[0] + a[1] + a[2] >= 200:
        print(3)
    elif a[1] + a[2] + a[3] >= 200:
        print(3)
    elif a[0] + a[1] + a[3] >= 200:
        print(3)
    elif a[0] + a[2] + a[3] >= 200:
        print(3)
    elif a[0] + a[1] >= 100:
        print(2)
    elif a[0] + a[2] >= 100:
        print(2)
    elif a[0] + a[3] >= 100:
        print(2)
    elif a[1] + a[2] >= 100:
        print(2)
    elif a[1] + a[3] >= 100:
        print(2)
    elif a[2] + a[3] >= 100:
        print(2)
    else:
        print(1)
main()
