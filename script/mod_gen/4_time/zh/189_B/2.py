def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        v_i,p_i = map(int,input().split())
        v.append(v_i)
        p.append(p_i)
    alcohol = 0
    for i in range(n):
        alcohol += v[i]*p[i]/100
        if alcohol > x:
            print(i+1)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()