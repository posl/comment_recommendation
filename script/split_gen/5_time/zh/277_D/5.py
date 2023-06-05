def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if n == 1:
        print(a[0])
        return
    if a[0] == 0:
        print(0)
        return
    if n == 2:
        if a[0] + 1 == a[1]:
            print(a[0])
        else:
            print(a[0] + 1)
        return
    if a[0] + 1 == a[1]:
        print(a[0])
        return
    if a[0] + 1 != a[1]:
        print(a[0] + 1)
        return
