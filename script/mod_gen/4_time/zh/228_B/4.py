def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    b = [0]*n
    for i in range(n):
        if a[i] != 0:
            b[a[i]-1] += 1
    for i in range(n):
        if b[i] != 0:
            a[i] = 0
    print(sum(a))

if __name__ == '__main__':
    main()