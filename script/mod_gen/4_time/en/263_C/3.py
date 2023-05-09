def solve():
    N, M = map(int, input().split())
    #print(N, M)
    for i in range(1, M+1):
        if N == 1:
            print(i)
        else:
            for j in range(1, M+1):
                if N == 2:
                    if i < j:
                        print(i, j)
                else:
                    for k in range(1, M+1):
                        if N == 3:
                            if j < k:
                                print(i, j, k)
                        else:
                            for l in range(1, M+1):
                                if N == 4:
                                    if k < l:
                                        print(i, j, k, l)
                                else:
                                    for m in range(1, M+1):
                                        if N == 5:
                                            if l < m:
                                                print(i, j, k, l, m)
                                        else:
                                            for n in range(1, M+1):
                                                if N == 6:
                                                    if m < n:
                                                        print(i, j, k, l, m, n)
                                                else:
                                                    for o in range(1, M+1):
                                                        if N == 7:
                                                            if n < o:
                                                                print(i, j, k, l, m, n, o)
                                                        else:
                                                            for p in range(1, M+1):
                                                                if N == 8:
                                                                    if o < p:
                                                                        print(i, j, k, l, m, n, o, p)
                                                                else:
                                                                    for q in range(1, M+1):
                                                                        if N == 9:
                                                                            if p < q:
                                                                                print(i, j, k, l, m, n, o, p, q)
                                                                        else:
                                                                            for r in range(1, M+1):
                                                                                if N == 10:
                                                                                    if q < r:
                                                                                        print(i, j, k, l, m, n, o, p, q, r)
    return 0

if __name__ == '__main__':
    solve()