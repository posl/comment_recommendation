def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        ans += ((N // a) + (0 if K % 2 else (N // (a * (K // 2))))) ** 3
    print(ans)

if __name__ == '__main__':
    main()