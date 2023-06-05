def main():
    n,k,a = map(int,input().split())
    if k%n == 0:
        print(a)
    else:
        print(k%n)

if __name__ == '__main__':
    main()