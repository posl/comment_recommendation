def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    A_sum_abs = sum(map(abs, A))
    A.sort()
    if N % 2 == 0:
        b = (A[N//2-1] + A[N//2]) // 2
        b2 = b + 1
        b1 = b - 1
        print(min(
            A_sum_abs - 2 * (A_sum - (b1 + 1) * N),
            A_sum_abs - 2 * (A_sum - (b2 + 1) * N)
        ))
    else:
        b = A[N//2]
        print(A_sum_abs - 2 * (A_sum - (b + 1) * N))

if __name__ == '__main__':
    main()