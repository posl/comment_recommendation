def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,t)
    #print(a)
    i = 0
    while t > 0:
        t -= a[i]
        i += 1
        if i == n:
            i = 0
    print(i,t+a[i-1])

if __name__ == '__main__':
    main()