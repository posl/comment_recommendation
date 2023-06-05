def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if a[i] == 1:
            b.append(i+1)
    m = len(b)
    if m == 0:
        print(0)
        return
    if m == 1:
        print(1)
        print(b[0])
        return
    if m == 2:
        print(2)
        print(b[0], b[1])
        return
    print(m)
    for i in range(m):
        print(b[i], end=' ')
    print()
