def main():
    n,k,a = map(int,input().split())
    print((a+k-1)%n)

if __name__ == '__main__':
    main()