def main():
    n,a,b = map(int,input().split())
    if a+b == 0:
        print(0)
    else:
        print((n//(a+b))*a+min(n%(a+b),a))

if __name__ == '__main__':
    main()