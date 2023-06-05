def main():
    K, X = map(int, input().split())
    for i in range(X-K+1, X+K):
        print(i, end=' ')
    print(X+K)

if __name__ == '__main__':
    main()