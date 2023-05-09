def main():
    K, X = map(int, input().split())
    print(*range(X-K+1, X+K))

if __name__ == '__main__':
    main()