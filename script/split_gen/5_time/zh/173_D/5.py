def main():
    N = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)
    sumB = 0
    for i in range(1, N):
        if i % 2 == 1:
            sumB += A[i]
    maxsumB = sumB
    for i in range(N):
        if i % 2 == 0:
            sumB += A[i]
        else:
            sumB -= A[i]
        maxsumB = max(maxsumB, sumB)
    print(sumA - maxsumB)
