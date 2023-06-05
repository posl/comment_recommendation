def main():
    N, M = map(int, input().split())
    u = []
    v = []
    for i in range(M):
        tmp = list(map(int, input().split()))
        u.append(tmp[0])
        v.append(tmp[1])
    #print(u)
    #print(v)
    #print(N, M)
    u_set = set(u)
    v_set = set(v)
    #print(u_set)
    #print(v_set)
    u_set = u_set & v_set
    #print(u_set)
    print(N*(N-1)//2 - M - len(u_set))

if __name__ == '__main__':
    main()