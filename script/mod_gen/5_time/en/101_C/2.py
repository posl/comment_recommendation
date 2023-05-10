def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    if (N - 1) % (K - 1) == 0:
        ans = (N - 1) // (K - 1)
    else:
        ans = (N - 1) // (K - 1) + 1
    print(ans)

if __name__ == '__main__':
    main()