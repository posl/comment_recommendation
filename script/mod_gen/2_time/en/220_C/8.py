def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    A_sum = sum(A)
    A_sum_100 = A_sum * 100
    A_sum_100_rest = X % A_sum_100
    A_sum_100_quotient = X // A_sum_100
    A_sum_100_rest_sum = 0
    A_sum_100_rest_sum_count = 0
    for i in range(N):
        A_sum_100_rest_sum += A[i]
        A_sum_100_rest_sum_count += 1
        if A_sum_100_rest_sum > A_sum_100_rest:
            break
    print(A_sum_100_quotient * N * 100 + A_sum_100_rest_sum_count)

if __name__ == '__main__':
    main()