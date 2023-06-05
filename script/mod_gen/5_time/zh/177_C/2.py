def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10**9 + 7
    sum_A = sum(A)
    sum_A2 = sum([a**2 for a in A])
    ans = (sum_A**2 - sum_A2) // 2 % mod
    print(ans)

if __name__ == '__main__':
    main()