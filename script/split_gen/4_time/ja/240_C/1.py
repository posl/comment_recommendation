def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    sum = 0
    for i in range(n):
        if (i + 1) % 2 == 0:
            sum += b[i]
        else:
            sum += a[i]
    if sum >= x:
        print('Yes')
    else:
        print('No')
