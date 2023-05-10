def main():
    K, X = map(int, input().split())
    result = []
    for i in range(X-K+1, X+K):
        result.append(i)
    print(*result)

if __name__ == '__main__':
    main()