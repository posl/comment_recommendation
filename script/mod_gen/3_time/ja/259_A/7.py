def main():
    n,m,x,t,d = map(int,input().split())
    a = t
    for i in range(m,x):
        a += d
    for i in range(x,n):
        a += d
    print(a)
main()

if __name__ == '__main__':
    main()