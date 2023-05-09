def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        print("Yes")
        return
    if n == 2:
        if a[0] == a[1]:
            print("Yes")
        else:
            print("No")
        return
    if k == 1:
        if sorted(a) == a:
            print("Yes")
        else:
            print("No")
        return
    if k == 2:
        if sorted(a[::2]) == a[::2] and sorted(a[1::2]) == a[1::2]:
            print("Yes")
        else:
            print("No")
        return
    if k == 3:
        if sorted(a[::3]) == a[::3] and sorted(a[1::3]) == a[1::3] and sorted(a[2::3]) == a[2::3]:
            print("Yes")
        else:
            print("No")
        return
    if k == 4:
        if sorted(a[::4]) == a[::4] and sorted(a[1::4]) == a[1::4] and sorted(a[2::4]) == a[2::4] and sorted(a[3::4]) == a[3::4]:
            print("Yes")
        else:
            print("No")
        return
    if k == 5:
        if sorted(a[::5]) == a[::5] and sorted(a[1::5]) == a[1::5] and sorted(a[2::5]) == a[2::5] and sorted(a[3::5]) == a[3::5] and sorted(a[4::5]) == a[4::5]:
            print("Yes")
        else:
            print("No")
        return
    if k == 6:
        if sorted(a[::6]) == a[::6] and sorted(a[1::6]) == a[1::6] and sorted(a[2::6]) == a[2::6] and sorted(a[3::6]) == a[3::6] and sorted(a[4::6]) == a[4::6] and sorted(a[5::6]) == a[5::6]:
