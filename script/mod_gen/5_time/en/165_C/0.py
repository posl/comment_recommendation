def main():
    n, m, q = map(int, input().split())
    a = [0]*q
    b = [0]*q
    c = [0]*q
    d = [0]*q
    for i in range(q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    ans = 0
    for i1 in range(1, m+1):
        for i2 in range(i1, m+1):
            for i3 in range(i2, m+1):
                for i4 in range(i3, m+1):
                    for i5 in range(i4, m+1):
                        for i6 in range(i5, m+1):
                            for i7 in range(i6, m+1):
                                for i8 in range(i7, m+1):
                                    for i9 in range(i8, m+1):
                                        for i10 in range(i9, m+1):
                                            tmp = 0
                                            for i in range(q):
                                                if i10 - i9 == c[i] and i9 - i8 == c[i] and i8 - i7 == c[i] and i7 - i6 == c[i] and i6 - i5 == c[i] and i5 - i4 == c[i] and i4 - i3 == c[i] and i3 - i2 == c[i] and i2 - i1 == c[i] and i1 - 1 == c[i]:
                                                    tmp += d[i]
                                            ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()