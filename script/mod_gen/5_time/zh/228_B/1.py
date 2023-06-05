def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    a = list(map(lambda x:x-1,a))
    b = [0]*n
    b[x-1] = 1
    for i in range(n):
        if b[i] == 1:
            b[a[i]] = 1
    print(sum(b))

if __name__ == '__main__':
    main()