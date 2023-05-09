def main():
    N, K = map(int, input().split())
    ans = N % K
    print(min(ans, abs(ans - K)))

if __name__ == '__main__':
    main()