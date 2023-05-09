def run():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        print(abs(a[0] + a[1]))
        return
    if n == 3:
        print(max(abs(a[0] + a[1]) + a[2], abs(a[0] + a[2]) + a[1], abs(a[1] + a[2]) + a[0]))
        return
    if n == 4:
        print(max(abs(a[0] + a[1]) + a[2] + a[3], abs(a[0] + a[1]) + abs(a[2] + a[3]), abs(a[0] + a[2]) + a[1] + a[3], abs(a[0] + a[2]) + abs(a[1] + a[3]), abs(a[0] + a[3]) + a[1] + a[2], abs(a[0] + a[3]) + abs(a[1] + a[2]), abs(a[1] + a[2]) + a[0] + a[3], abs(a[1] + a[2]) + abs(a[0] + a[3]), abs(a[1] + a[3]) + a[0] + a[2], abs(a[1] + a[3]) + abs(a[0] + a[2]), abs(a[2] + a[3]) + a[0] + a[1], abs(a[2] + a[3]) + abs(a[0] + a[1])))
        return
    if n == 5:
        print(max(abs(a[0] + a[1]) + abs(a[2] + a[3]) + a[4], abs(a[0] + a[1]) + abs(a[2] + a[4]) + a[3], abs(a[0] + a[1]) + abs(a[3] + a[4]) + a[2], abs(a[0] + a[2]) + abs(a[1] + a[3]) + a[4], abs(a[0] + a[2]) + abs(a[1] + a[4]) + a[3], abs(a
