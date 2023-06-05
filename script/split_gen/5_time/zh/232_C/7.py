def main():
    n, m = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    for i in range(m):
        c1, d1 = map(int, input().split())
        c.append(c1)
        d.append(d1)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (i + 1 in a and j + 1 in b) or (i + 1 in b and j + 1 in a):
                if not ((i + 1 in c and j + 1 in d) or (i + 1 in d and j + 1 in c)):
                    print('No')
                    return
            if (i + 1 in c and j + 1 in d) or (i + 1 in d and j + 1 in c):
                if not ((i + 1 in a and j + 1 in b) or (i + 1 in b and j + 1 in a)):
                    print('No')
                    return
    print('Yes')
