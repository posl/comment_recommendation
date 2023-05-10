def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    max_A = max(A)
    min_A = min(A)
    if M == 1:
        print(sum_A)
    elif max_A <= 0:
        print(max_A * M)
    elif min_A >= 0:
        print(sum_A + (M - 2) * min_A)
    else:
        A.sort(reverse=True)
        sum_A = 0
        for i in range(M):
            sum_A += A[i]
        print(sum_A + (M - 1) * min_A)
