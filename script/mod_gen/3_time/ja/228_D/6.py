def main():
    q = int(input())
    a = [-1]*1048576
    for i in range(q):
        t,x = map(int,input().split())
        if t == 1:
            h = x
            while a[h%1048576] != -1:
                h += 1
            a[h%1048576] = x
        else:
            print(a[x%1048576])

if __name__ == '__main__':
    main()