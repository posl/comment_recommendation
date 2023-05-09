def main():
    N, K = map(int, input().split())
    print(N * K * 100 + N * K * 10 + N * K)

if __name__ == '__main__':
    main()