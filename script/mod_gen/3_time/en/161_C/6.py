def main():
    N, K = map(int, input().split())
    ans = min(N%K, abs(N%K-K))
    print(ans)

if __name__ == '__main__':
    main()