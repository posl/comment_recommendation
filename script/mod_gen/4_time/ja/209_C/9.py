def main():
    # Input
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    # Solve
    ans = 1
    for i in range(N):
        ans *= (C[i] - i)
        ans %= (10 ** 9 + 7)
    # Output
    print(ans)

if __name__ == '__main__':
    main()