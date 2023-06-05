def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        x.append(tmp[0])
        y.append(tmp[1])
    print(a)
    print(x)
    print(y)

if __name__ == '__main__':
    main()