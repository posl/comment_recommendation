def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    if N % K == 0:
        ans = 0
    else:
        ans = 1
    print(ans + N // K)

if __name__ == '__main__':
    main()