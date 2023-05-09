def main():
    N,K = map(int, input().split())
    for i in range(K):
        N = f(N)
    print(N)

if __name__ == '__main__':
    main()