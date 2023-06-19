def main():
    n,a,b = map(int,input().split())
    if a+b == 0:
        print(0)
        return
    else:
        if n%(a+b) > a:
            print(a*(n//(a+b))+a)
        else:
            print(a*(n//(a+b))+n%(a+b))

if __name__ == '__main__':
    main()