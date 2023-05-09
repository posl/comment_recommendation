def main():
    N, M = map(int, input().split())
    for i in range(1, M+1):
        if N == 1:
            print(i)
        else:
            for j in range(i+1, M+1):
                if N == 2:
                    print(i, j)
                else:
                    for k in range(j+1, M+1):
                        if N == 3:
                            print(i, j, k)
                        else:
                            for l in range(k+1, M+1):
                                if N == 4:
                                    print(i, j, k, l)
                                else:
                                    for m in range(l+1, M+1):
                                        if N == 5:
                                            print(i, j, k, l, m)
                                        else:
                                            for n in range(m+1, M+1):
                                                if N == 6:
                                                    print(i, j, k, l, m, n)
                                                else:
                                                    for o in range(n+1, M+1):
                                                        if N == 7:
                                                            print(i, j, k, l, m, n, o)
                                                        else:
                                                            for p in range(o+1, M+1):
                                                                if N == 8:
                                                                    print(i, j, k, l, m, n, o, p)
                                                                else:
                                                                    for q in range(p+1, M+1):
                                                                        if N == 9:
                                                                            print(i, j, k, l, m, n, o, p, q)
                                                                        else:
                                                                            for r in range(q+1, M+1):
                                                                                if N == 10:
                                                                                    print(i, j, k, l, m, n, o, p, q, r)

if __name__ == '__main__':
    main()