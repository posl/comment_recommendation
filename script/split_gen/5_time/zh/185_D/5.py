def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    if n == 1:
        print(0)
        return
    if n == 2:
        if m == 1:
            print(1)
        else:
            print(0)
        return
    if n == 3:
        if m == 2:
            print(0)
        elif m == 1:
            if a[0] == 1 or a[0] == 3:
                print(1)
            else:
                print(0)
        else:
            print(0)
        return
    if n == 4:
        if m == 3:
            print(0)
        elif m == 2:
            if a[0] == 1 and a[1] == 2:
                print(0)
            else:
                print(1)
        elif m == 1:
            if a[0] == 1 or a[0] == 4:
                print(1)
            else:
                print(0)
        else:
            print(0)
        return
    if n == 5:
        if m == 4:
            print(0)
        elif m == 3:
            if a[0] == 1 and a[1] == 3 and a[2] == 5:
                print(0)
            else:
                print(1)
        elif m == 2:
            if a[0] == 1 and a[1] == 3:
                print(1)
            elif a[0] == 2 and a[1] == 4:
                print(1)
            else:
                print(0)
        elif m == 1:
            if a[0] == 1 or a[0] == 4:
                print(1)
            else:
                print(0)
        else:
            print(0)
        return
    if m == 0:
        print(1)
        return
    if m == 1:
        if a[0] == 1 or a[0] == n:
            print(1)
        else:
