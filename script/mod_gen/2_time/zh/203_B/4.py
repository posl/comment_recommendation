def main():
    n,k = map(int, input().split())
    print(100 * n * (n+1) * k // 2)

if __name__ == '__main__':
    main()