def main():
    N, D = map(int, input().split())
    print((N-1)//(D*2+1)+1)

if __name__ == '__main__':
    main()