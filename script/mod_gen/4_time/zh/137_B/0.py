def main():
    K, X = map(int, input().split())
    result = [X]
    for i in range(1, K):
        result.append(X - i)
        result.append(X + i)
    result.sort()
    print(*result)

if __name__ == '__main__':
    main()