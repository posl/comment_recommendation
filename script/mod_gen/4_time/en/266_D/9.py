def main():
    N = int(input())
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        A.append((t, x, a))
    B = []
    C = []
    for t, x, a in A:
        if x == 0:
            B.append((t, a))
        else:
            C.append((t, x, a))
    B.sort()
    C.sort()
    D = []
    for t, a in B:
        D.append((t, a))
    for t, x, a in C:
        D.append((t, a))
    D.sort()
    T = 0
    X = 0
    Y = 0
    for t, a in D:
        if t > T:
            if X > 0:
                Y += a
                X -= 1
                T = t
        if t == T:
            if X == 0:
                X = 4
                Y += a
                T += 1
                X -= 1
    print(Y)

if __name__ == '__main__':
    main()