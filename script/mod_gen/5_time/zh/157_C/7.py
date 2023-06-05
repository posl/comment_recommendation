def main():
    n,m = map(int,input().split())
    d = [10**i for i in range(n)]
    a = [0]*n
    for i in range(m):
        s,c = map(int,input().split())
        a[s-1] = c
    for i in range(10**n):
        t = i
        for j in range(n):
            if (t//d[j])%10 != a[j]:
                break
        else:
            print(i)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()