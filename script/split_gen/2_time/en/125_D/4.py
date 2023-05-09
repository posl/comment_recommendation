def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        print(max(a[0], a[1]))
        return
    if n == 3:
        print(max(a[0] + a[1], a[1] + a[2], a[0] + a[2]))
        return
    if n == 4:
        print(max(a[0] + a[1] + a[2], a[0] + a[1] + a[3], a[0] + a[2] + a[3], a[1] + a[2] + a[3]))
        return
    if n == 5:
        print(max(a[0] + a[1] + a[2] + a[3], a[0] + a[1] + a[2] + a[4], a[0] + a[1] + a[3] + a[4], a[0] + a[2] + a[3] + a[4], a[1] + a[2] + a[3] + a[4]))
        return
    if n == 6:
        print(max(a[0] + a[1] + a[2] + a[3] + a[4], a[0] + a[1] + a[2] + a[3] + a[5], a[0] + a[1] + a[2] + a[4] + a[5], a[0] + a[1] + a[3] + a[4] + a[5], a[0] + a[2] + a[3] + a[4] + a[5], a[1] + a[2] + a[3] + a[4] + a[5]))
        return
    if n == 7:
        print(max(a[0] + a[1] + a[2] + a[3] + a[4] + a[5], a[0] + a[1] + a[2] + a[3] + a[4] + a[6], a[0] + a[1] + a[2] + a[3
