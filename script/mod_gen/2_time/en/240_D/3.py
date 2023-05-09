def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * 10**5 + 1)
    for i in range(N):
        B[A[i]] += 1
    ans = 0
    for i in range(2 * 10**5 + 1):
        ans += B[i] % 2
    print(ans)

if __name__ == '__main__':
    main()