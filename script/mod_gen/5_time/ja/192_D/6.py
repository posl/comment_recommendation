def solve(X, M):
    d = int(max(X))
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    else:
        #Xを10進法表記とみなして得られる値を求める
        X10 = 0
        for i in range(len(X)):
            X10 += int(X[i]) * (d ** (len(X)-i-1))
        #XをXの最大値+1進法表記とみなして得られる値を求める
        X11 = 0
        for i in range(len(X)):
            X11 += int(X[i]) * ((d+1) ** (len(X)-i-1))
        #XをXの最大値+2進法表記とみなして得られる値を求める
        X12 = 0
        for i in range(len(X)):
            X12 += int(X[i]) * ((d+2) ** (len(X)-i-1))
        #XをXの最大値+3進法表記とみなして得られる値を求める
        X13 = 0
        for i in range(len(X)):
            X13 += int(X[i]) * ((d+3) ** (len(X)-i-1))
        #XをXの最大値+4進法表記とみなして得られる値を求める
        X14 = 0
        for i in range(len(X)):
            X14 += int(X[i]) * ((d+4) ** (len(X)-i-1))
        #XをXの最大値+5進法表記とみなして得られる値を求める
        X15 = 0
        for i in range(len(X)):
            X15 += int(X[i]) * ((d+5) ** (len(X)-i-1))
        #XをXの最大値+6進法表記とみなして得られる値を求める
        X16 = 0
        for i in range(len

if __name__ == '__main__':
    solve()