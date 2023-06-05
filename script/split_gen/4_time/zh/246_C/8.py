def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k >= n:
        print(0)
        return
    if k == 1:
        print(a[0])
        return
    if k == 2:
        print(a[1])
        return
    if k == 3:
        print(a[1]+a[0])
        return
    if k == 4:
        print(a[2]+a[1])
        return
    if k == 5:
        print(a[2]+a[1]+a[0])
        return
    if k == 6:
        print(a[3]+a[2])
        return
    if k == 7:
        print(a[3]+a[2]+a[1])
        return
    if k == 8:
        print(a[3]+a[2]+a[1]+a[0])
        return
    if k == 9:
        print(a[4]+a[3])
        return
    if k == 10:
        print(a[4]+a[3]+a[2])
        return
    if k == 11:
        print(a[4]+a[3]+a[2]+a[1])
        return
    if k == 12:
        print(a[4]+a[3]+a[2]+a[1]+a[0])
        return
    if k == 13:
        print(a[5]+a[4])
        return
    if k == 14:
        print(a[5]+a[4]+a[3])
        return
    if k == 15:
        print(a[5]+a[4]+a[3]+a[2])
        return
    if k == 16:
        print(a[5]+a[4]+a[3]+a[2]+a[1])
        return
    if k == 17:
        print(a[5]+a[4]+a[3]+a[2]+a[1]+a[0])
        return
    if k == 18:
        print(a[6]+a[5])
        return
    if k == 19:
        print(a[6]+a[5]+a[4])
        return
