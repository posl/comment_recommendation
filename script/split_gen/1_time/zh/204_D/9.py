def main():
    n = int(input())
    t = [int(i) for i in input().split()]
    t.sort()
    if n == 1:
        print(t[0])
        return
    if n == 2:
        print(max(t))
        return
    if n == 3:
        print(max(t[0] + t[1], t[2]))
        return
    if n == 4:
        print(max(t[0] + t[3], t[1] + t[2]))
        return
    if n == 5:
        print(max(t[0] + t[4], t[1] + t[3], t[2]))
        return
    if n == 6:
        print(max(t[0] + t[5], t[1] + t[4], t[2] + t[3]))
        return
    if n == 7:
        print(max(t[0] + t[6], t[1] + t[5], t[2] + t[4], t[3]))
        return
    if n == 8:
        print(max(t[0] + t[7], t[1] + t[6], t[2] + t[5], t[3] + t[4]))
        return
    if n == 9:
        print(max(t[0] + t[8], t[1] + t[7], t[2] + t[6], t[3] + t[5], t[4]))
        return
