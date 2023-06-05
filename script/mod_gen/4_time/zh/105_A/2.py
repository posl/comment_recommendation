def main():
    N,K = map(int,input().split())
    print(N-K if K>1 else 0)

if __name__ == '__main__':
    main()