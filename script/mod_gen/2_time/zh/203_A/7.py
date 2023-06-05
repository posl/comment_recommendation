def calc(a, b, k):
    if a == 0:
        return 'b' * b
    elif b == 0:
        return 'a' * a
    else:
        comb = [[0 for i in range(b+1)] for j in range(a+1)]
        for i in range(a+1):
            comb[i][0] = 1
        for i in range(1, a+1):
            for j in range(1, b+1):
                comb[i][j] = comb[i-1][j] + comb[i][j-1]
        if k <= comb[a-1][b]:
            return 'a' + calc(a-1, b, k)
        else:
            return 'b' + calc(a, b-1, k-comb[a-1][b])

if __name__ == '__main__':
    calc()