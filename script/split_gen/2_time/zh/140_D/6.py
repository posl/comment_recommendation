def main():
    N = int(input())
    B = [int(i) for i in input().split()]
    A = [0 for i in range(N)]
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    print(sum(A))
