def main():
    N, K = map(int, input().split())
    print(N//K * N//K * N//K + (N//K+1)**3 if K%2 == 0 else N//K * N//K * N//K)

if __name__ == '__main__':
    main()