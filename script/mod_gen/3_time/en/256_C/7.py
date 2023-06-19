def solve():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    n = 0
    for a in range(1, 31):
        for b in range(1, 31):
            for c in range(1, 31):
                for d in range(1, 31):
                    for e in range(1, 31):
                        for f in range(1, 31):
                            for g in range(1, 31):
                                for i in range(1, 31):
                                    for j in range(1, 31):
                                        if h[0]==a+d+g and h[1]==b+e+h and h[2]==c+f+i and w[0]==a+b+c and w[1]==d+e+f and w[2]==g+h+i:
                                            n += 1
    print(n)
solve()
