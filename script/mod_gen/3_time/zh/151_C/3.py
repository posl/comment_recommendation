def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = ['']*n
    for i in range(m):
        p[i],s[i] = input().split()
        p[i] = int(p[i])
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            if p[i] == 1:
                ac += 1
            else:
                if p[i] in p[:i]:
                    continue
                else:
                    ac += 1
                    wa += p[:i].count(p[i])
        else:
            if p[i] == 1:
                wa += 1
            else:
                if p[i] in p[:i]:
                    continue
                else:
                    wa += p[:i].count(p[i])
    print(ac,wa)

if __name__ == '__main__':
    main()