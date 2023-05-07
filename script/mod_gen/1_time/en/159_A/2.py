def main():
    n,m = map(int,input().split())
    if n == 0:
        print(m)
    elif m == 0:
        print(n)
    else:
        print(n*m)

if __name__ == '__main__':
    main()