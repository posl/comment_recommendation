def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    c = [x for _,x in sorted(zip(a,b))]
    d = [x for _,x in sorted(zip(a,a))]
    a = d
    b = c
    sum = 0
    j = 0
    for i in range(m):
        if j < n and a[j] <= i+1:
            sum += b[j]
            j += 1
    print(sum)

if __name__ == '__main__':
    main()