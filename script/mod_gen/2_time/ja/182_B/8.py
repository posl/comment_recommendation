def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A_max = A[0]
    A_max_gcd = 0
    for i in range(2, A_max+1):
        gcd = 0
        for j in range(N):
            if A[j] % i == 0:
                gcd += 1
        if gcd > A_max_gcd:
            A_max_gcd = gcd
            A_max_gcd_num = i
    print(A_max_gcd_num)

if __name__ == '__main__':
    main()