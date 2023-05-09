def main():
    N,M = map(int,input().split())
    p = []
    s = []
    for i in range(M):
        p_i,s_i = input().split()
        p.append(int(p_i))
        s.append(s_i)
    AC = [0]*N
    WA = [0]*N
    for i in range(M):
        if s[i] == 'AC':
            AC[p[i]-1] = 1
        else:
            if AC[p[i]-1] == 0:
                WA[p[i]-1] += 1
    print(sum(AC),sum([AC[i]*WA[i] for i in range(N)]))

if __name__ == '__main__':
    main()