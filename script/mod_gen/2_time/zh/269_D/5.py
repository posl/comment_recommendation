def main():
    n = int(input())
    nbin = bin(n)[2:]
    nlen = len(nbin)
    ans = []
    for i in range(1 << nlen):
        x = bin(i)[2:]
        xlen = len(x)
        if xlen > nlen:
            break
        ok = True
        for j in range(xlen):
            if x[j] == '1' and nbin[nlen - xlen + j] == '0':
                ok = False
                break
        if ok:
            ans.append(i)
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()