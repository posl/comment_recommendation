def main():
    n,a,x,y = map(int,input().split())
    if n < a:
        print(n*x)
    else:
        print((n-a)*y+a*x)

if __name__ == '__main__':
    main()