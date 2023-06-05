def check(p):
    y = [0]*(N+1)
    y[0] = p[0]
    for i in range(1,N+1):
        if S[i-1] == "AND":
            y[i] = y[i-1] and p[i]
        else:
            y[i] = y[i-1] or p[i]
    return y[N]

if __name__ == '__main__':
    check()