def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    # print(N)
    # print(A)
    # print(X)
    sum_A = sum(A)
    # print(sum_A)
    div, mod = divmod(X, sum_A)
    # print(div, mod)
    sum_B = sum_A * div
    # print(sum_B)
    n = 0
    sum_B += A[n]
    # print(sum_B)
    while sum_B <= X:
        n += 1
        sum_B += A[n]
        # print(sum_B)
    print(div * N + n + 1)
main()
