def main():
    n,k,a = map(int,input().split())
    if n == a:
        print(k%n)
    else:
        if k%n == 0:
            print(n)
        else:
            print(k%n)

if __name__ == '__main__':
    main()