def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        a,b = map(int,input().split())
        v.append(a)
        p.append(b)
    sum = 0
    for i in range(n):
        sum += v[i] * p[i] / 100
        if sum > x:
            print(i+1)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()