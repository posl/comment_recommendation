def main():
    n,m = map(int,input().split())
    l = []
    r = []
    for i in range(m):
        a,b = map(int,input().split())
        l.append(a)
        r.append(b)
    l_max = max(l)
    r_min = min(r)
    if r_min-l_max+1 >= 0:
        print(r_min-l_max+1)
    else:
        print(0)

if __name__ == '__main__':
    main()