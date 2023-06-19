def calculate(A, b):
    sum = 0
    for i in range(0, len(A)):
        sum += abs(A[i] - (b + i + 1))
    return sum
N = int(input())
A = list(map(int, input().split()))
A.sort()
b = A[N//2]
print(calculate(A, b))
