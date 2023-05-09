def main():
    n,m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    for i in range(10 ** n):
        sflg = True
        for j in range(m):
            if int(str(i)[s[j] - 1]) != c[j]:
                sflg = False
                break
        if sflg:
            print(i)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()