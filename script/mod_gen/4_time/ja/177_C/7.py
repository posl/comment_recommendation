def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    sumA = sum(A)
    for a in A:
        sumA -= a
        ans += a * sumA
    print(ans % mod)

if __name__ == '__main__':
    main()