def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a.sort()
    b.sort()
    if a[0] == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()