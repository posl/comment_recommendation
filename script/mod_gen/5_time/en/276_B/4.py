def main():
    n,m = map(int, input().split())
    l = []
    for i in range(m):
        a,b = map(int, input().split())
        l.append(a)
        l.append(b)
    for i in range(1,n+1):
        print(l.count(i))

if __name__ == '__main__':
    main()