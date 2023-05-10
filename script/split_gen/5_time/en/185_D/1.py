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
        print(1)
        return
    if a[0] != 1:
        a.insert(0, 0)
    if a[m-1] != n:
        a.append(n+1)
    k = []
    for i in range(m+1):
        k.append(a[i+1] - a[i] - 1)
    k = list(filter(lambda x: x > 0, k))
    k.sort()
    if len(k) == 0:
        print(0)
        return
    if k[0] == 0:
        print(1)
        return
    if len(k) == 1:
        print(k[0])
        return
    if k[0] == 1:
        print(len(k))
        return
    if k[0] == 2:
        print(len(k)+1)
        return
    if k[0] == 3:
        print(len(k)+2)
        return
    if k[0] == 4:
        print(len(k)+3)
        return
    if k[0] == 5:
        print(len(k)+4)
        return
    if k[0] == 6:
        print(len(k)+5)
        return
    if k[0] == 7:
        print(len(k)+6)
        return
    if k[0] == 8:
        print(len(k)+7)
        return
    if k[0] == 9:
        print(len(k)+8)
        return
    if k[0] == 10:
        print(len(k)+9)
        return
    if k[0] == 11:
        print(len(k)+10)
        return
    if k[0] == 12:
        print(len(k)+11)
        return
    if k[0] == 13:
        print(len(k)+12)
        return
    if k[0] == 14:
        print(len(k)+13)
        return
    if k[0] == 15:
        print
