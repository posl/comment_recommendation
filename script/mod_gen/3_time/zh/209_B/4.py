def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if i % 2 == 1:
            a[i] = a[i] - 1
    if sum(a) <= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()