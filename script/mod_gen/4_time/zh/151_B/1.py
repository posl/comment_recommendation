def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = N * M - S
    if ans > K:
        print(-1)
    elif ans < 0:
        print(0)
    else:
        print(ans)

if __name__ == '__main__':
    main()