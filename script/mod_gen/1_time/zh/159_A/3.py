def main():
    N,M = map(int,input().split())
    print(N*(N-1)//2+M*(M-1)//2)

if __name__ == '__main__':
    main()