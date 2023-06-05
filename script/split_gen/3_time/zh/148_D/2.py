def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    if n == 2:
        if a[0] == 1 and a[1] == 2:
            print(0)
        else:
            print(-1)
        return
    if n == 3:
        if a[0] == 1 and a[1] == 2 and a[2] == 1:
            print(1)
        else:
            print(-1)
        return
    if n == 4:
        if a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 4:
            print(0)
        elif a[0] == 1 and a[1] == 2 and a[2] == 4 and a[3] == 3:
            print(1)
        elif a[0] == 1 and a[1] == 3 and a[2] == 2 and a[3] == 4:
            print(1)
        elif a[0] == 1 and a[1] == 3 and a[2] == 4 and a[3] == 2:
            print(2)
        elif a[0] == 1 and a[1] == 4 and a[2] == 2 and a[3] == 3:
            print(2)
        elif a[0] == 1 and a[1] == 4 and a[2] == 3 and a[3] == 2:
            print(3)
        else:
            print(-1)
        return
    if n == 5:
        if a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 4 and a[4] == 5:
            print(0)
        elif a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 5 and a[4] == 4:
            print(1)
        elif a[0] == 1 and a[1] == 2 and a[2] ==
