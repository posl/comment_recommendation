def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    d = {}
    for i in range(n-1):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
        if b[i] in d:
            d[b[i]] += 1
        else:
            d[b[i]] = 1
    for i in range(1, n+1):
        if i not in d:
            print('No')
            return
    print('Yes')
