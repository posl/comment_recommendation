def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    total = 0
    for i in range(n):
        total += a[i] * b[i]
    if total <= x:
        print('Yes')
    else:
        print('No')
