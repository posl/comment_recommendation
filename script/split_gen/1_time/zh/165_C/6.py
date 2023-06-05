def main():
    n, m, q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    max_score = 0
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
                                            score = 0
                                            for i in range(q):
                                                if (b[i] == 1):
                                                    if (i1 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 2):
                                                    if (i2 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 3):
                                                    if (i3 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 4):
                                                    if (i4 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 5):
                                                    if (i5 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 6):
                                                    if (i6 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 7):
                                                    if (i7 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 8):
                                                    if (i8 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 9):
                                                    if (i9 - i1 == c[i]):
                                                        score += d[i]
                                                elif (b[i] == 10):
                                                    if (i10
