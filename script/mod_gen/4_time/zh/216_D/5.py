def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        k = int(input())
        a.append(list(map(int,input().split())))
    print(a)
    #print(n,m,a)

if __name__ == '__main__':
    main()