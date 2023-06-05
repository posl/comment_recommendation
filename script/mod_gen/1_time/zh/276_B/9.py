def main():
    n,m = map(int,input().split())
    a = [0]*n
    b = [0]*n
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    for i in range(n):
        count = 0
        for j in range(m):
            if a[j] == i+1:
                count += 1
            elif b[j] == i+1:
                count += 1
        print(count,end=' ')
        for j in range(m):
            if a[j] == i+1:
                print(b[j],end=' ')
            elif b[j] == i+1:
                print(a[j],end=' ')
        print()

if __name__ == '__main__':
    main()