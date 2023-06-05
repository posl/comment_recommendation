def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i-1 for i in a]
    f = [0]*n
    f[x-1] = 1
    for i in range(n):
        if f[i] == 1:
            f[a[i]] = 1
    print(sum(f))

if __name__ == '__main__':
    main()