def main():
    N, K = map(int, input().split())
    ans = N % K
    ans = min(ans, abs(ans-K))
    print(ans)
main()

if __name__ == '__main__':
    main()