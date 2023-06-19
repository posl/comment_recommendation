def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = sorted(zip(b, a))
    t = 0
    for i in range(n):
        t += c[i][1]
        if t > c[i][0]:
            print('No')
            exit()
    print('Yes')
