def getMinMP(N, A, B, C, l):
    minMP = 10000
    for i in range(2**N):
        if i == 0:
            continue
        mp = 0
        a = []
        b = []
        c = []
        for j in range(N):
            if (i >> j) & 1:
                a.append(l[j])
            else:
                b.append(l[j])
        for k in range(len(a)):
            mp += a[k]
        for k in range(len(b)):
            mp += b[k]
        if A in a and B in a and C in a:
            mp -= 30
        if A in b and B in b and C in b:
            mp -= 30
        if A in a and B in b and C in b:
            mp -= 10
        if A in b and B in a and C in b:
            mp -= 10
        if A in b and B in b and C in a:
            mp -= 10
        if A in a and B in a and C in b:
            mp -= 10
        if A in b and B in a and C in a:
            mp -= 10
        if A in a and B in b and C in a:
            mp -= 10
        if A in a and B in a and C in a:
            mp -= 20
        if A in b and B in b and C in b:
            mp -= 20
        if mp < minMP:
            minMP = mp
    return minMP
