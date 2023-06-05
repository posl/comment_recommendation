def main():
    n,k,a = map(int,input().split())
    k = k%n
    if k+a-1 > n:
        print(k+a-n)
    else:
        print(k+a-1)

if __name__ == '__main__':
    main()