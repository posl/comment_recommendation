def main():
    n,m,x,t,d = map(int,input().split())
    a = t
    for i in range(x,m):
        a = a + d
    print(a)

if __name__ == '__main__':
    main()