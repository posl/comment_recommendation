def main():
    N = int(input())
    a = [0] * (N - 1)
    b = [0] * (N - 1)
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())
    #print(a, b)
    if N == 3:
        print("Yes")
        return
    if N == 4:
        if a.count(a[0]) == 2 and b.count(a[0]) == 2:
            print("Yes")
            return
        if a.count(b[0]) == 2 and b.count(b[0]) == 2:
            print("Yes")
            return
        print("No")
        return
    if N == 5:
        if a.count(a[0]) == 2 and b.count(a[0]) == 3:
            print("Yes")
            return
        if a.count(b[0]) == 2 and b.count(b[0]) == 3:
            print("Yes")
            return
        print("No")
        return
    if N == 6:
        if a.count(a[0]) == 2 and b.count(a[0]) == 4:
            print("Yes")
            return
        if a.count(b[0]) == 2 and b.count(b[0]) == 4:
            print("Yes")
            return
        print("No")
        return
    if N == 7:
        if a.count(a[0]) == 2 and b.count(a[0]) == 5:
            print("Yes")
            return
        if a.count(b[0]) == 2 and b.count(b[0]) == 5:
            print("Yes")
            return
        print("No")
        return
    if N == 8:
        if a.count(a[0]) == 2 and b.count(a[0]) == 6:
            print("Yes")
            return
        if a.count(b[0]) == 2 and b.count(b[0]) == 6:
            print("Yes")
            return
        print("No")
        return
    if N == 9:
        if a.count(a[0]) == 2 and b.count(a[0]) == 7:
            print("Yes")
            return
        if a.count(b[0
