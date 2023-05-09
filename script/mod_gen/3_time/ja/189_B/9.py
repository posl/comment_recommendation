def main():
    # input
    n, x = map(int, input().split())
    #print(n, x)
    v = []
    p = []
    for i in range(n):
        v_tmp, p_tmp = map(int, input().split())
        v.append(v_tmp)
        p.append(p_tmp)
    #print(v)
    #print(p)
    # compute
    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
            print(i+1)
            exit()
    print(-1)

if __name__ == '__main__':
    main()