def main():
    N,M = map(int,input().split())
    print((N-1)*N//2 + (M-1)*M//2)

if __name__ == '__main__':
    main()