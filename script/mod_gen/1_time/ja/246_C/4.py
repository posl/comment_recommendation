def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans += max(a - K*X, 0)
    print(ans)

if __name__ == '__main__':
    main()