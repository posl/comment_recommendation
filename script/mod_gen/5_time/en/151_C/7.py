def main():
    n,m = map(int,input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi,si = input().split()
        p[int(pi)-1] += 1
        s[int(pi)-1] = si
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == 'AC':
            ac += 1
            wa += p[i]
    print(ac,wa)

if __name__ == '__main__':
    main()