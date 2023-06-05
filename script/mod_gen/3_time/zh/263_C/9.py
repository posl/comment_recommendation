def main():
    n,m = map(int,input().split())
    a = [1]*n
    while True:
        for i in range(n):
            print(a[i],end=' ')
        print()
        i = n-1
        while i>=0 and a[i] == m:
            i -= 1
        if i<0:
            break
        a[i] += 1
        for j in range(i+1,n):
            a[j] = a[i]

if __name__ == '__main__':
    main()