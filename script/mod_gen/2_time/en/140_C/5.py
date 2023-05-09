def max_sum(A):
    N = len(A)
    B = [0] * N
    B[0] = A[0]
    B[N-1] = A[N-2]
    for i in range(1,N-1):
        B[i] = min(A[i-1], A[i])
    return sum(B)
N = int(input())
A = list(map(int, input().split()))
print(max_sum(A))

if __name__ == '__main__':
    max_sum()