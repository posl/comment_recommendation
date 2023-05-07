def main():
    N, K = map(int, input().split())
    ans = N % K
    ans = min(ans, K - ans)
    print(ans)

if __name__ == '__main__':
    main()