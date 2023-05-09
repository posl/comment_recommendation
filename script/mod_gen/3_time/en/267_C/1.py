def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, sum([x * (i + 1) for i, x in enumerate(A[i:i + M])]))
    print(ans)

if __name__ == '__main__':
    main()