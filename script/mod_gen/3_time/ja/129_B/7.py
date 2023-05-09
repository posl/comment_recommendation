def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1000000000
    for i in range(N - 1):
        S1 = sum(A[:i + 1])
        S2 = sum(A[i + 1:])
        ans = min(ans, abs(S1 - S2))
    print(ans)

if __name__ == '__main__':
    main()