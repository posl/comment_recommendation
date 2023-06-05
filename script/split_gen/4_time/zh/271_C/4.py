def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = list(set(a))
    if len(a) == 1:
        print(0)
        return
    if len(a) == 2:
        if a[1] == a[0] * 2:
            print(0)
            return
        else:
            print(1)
            return
    if len(a) == 3:
        if a[1] == a[0] * 2 and a[2] == a[0] * 3:
            print(0)
            return
        if a[1] == a[0] * 2 and a[2] != a[0] * 3:
            print(1)
            return
        if a[1] != a[0] * 2 and a[2] == a[0] * 3:
            print(1)
            return
        if a[1] != a[0] * 2 and a[2] != a[0] * 3:
            print(2)
            return
    if len(a) >= 4:
        if a[1] == a[0] * 2:
            print(1)
            return
        else:
            print(2)
            return
