def main():
    n,a,b = map(int,input().split())
    if a*n < b:
        print(a*n)
    else:
        print(b)

if __name__ == '__main__':
    main()