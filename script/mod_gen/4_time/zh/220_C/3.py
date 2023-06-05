def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sum_A = sum(A)
    if X <= sum_A:
        print(1)
        return
    B = A * 100
    sum_B = sum_A * 100
    for i in range(1, N * 100):
        B.append(B[i - 1])
        sum_B += B[i - 1]
        if sum_B > X:
            print(i + 1)
            return
solve()
