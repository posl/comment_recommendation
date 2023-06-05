def main():
    n,m = map(int,input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        k.append(list(map(int,input().split())))
    for i in range(m):
        p.append(list(map(int,input().split())))
    print(k)
    print(p)

if __name__ == '__main__':
    main()