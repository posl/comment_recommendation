def main():
    N,M = map(int,input().split())
    s = []
    c = []
    for i in range(M):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)
    for i in range(10**(N-1),10**N):
        s_i = str(i)
        flag = True
        for j in range(M):
            if int(s_i[s[j]-1]) != c[j]:
                flag = False
                break
        if flag:
            print(i)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()