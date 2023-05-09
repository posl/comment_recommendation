def main():
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]*n
    for i in range(n):
        if i+1 in range(p,q+1):
            b[i] = a[i+r-q-1]
        elif i+1 in range(r,s+1):
            b[i] = a[i+q-p+1]
        else:
            b[i] = a[i]
    print(*b)

if __name__ == '__main__':
    main()