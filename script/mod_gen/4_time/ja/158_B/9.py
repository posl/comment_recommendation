def main():
    n,a,b = map(int, input().split())
    #print(n,a,b)
    if a+b == 0:
        print(0)
        exit()
    if a == 0:
        print(n)
        exit()
    if n == 1:
        print(1)
        exit()
    if a+b > n:
        print(n)
        exit()
    if a+b == n:
        print(a)
        exit()
    if a+b < n:
        print(a)
        exit()

if __name__ == '__main__':
    main()