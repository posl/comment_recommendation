def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    sum_A = sum(A)
    sum_A2 = sum([a*a for a in A])
    print((sum_A*sum_A-sum_A2)//2%MOD)

if __name__ == '__main__':
    main()