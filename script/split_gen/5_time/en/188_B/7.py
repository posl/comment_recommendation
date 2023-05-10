def inner_product(A, B):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    return sum
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
