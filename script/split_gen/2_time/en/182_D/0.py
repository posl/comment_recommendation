def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        if A[0] >= 0:
            print(A[0])
        else:
            print(0)
    else:
        if A[0] < 0:
            A[0] = 0
        for i in range(1, N):
            A[i] += A[i-1]
            if A[i] < 0:
                A[i] = 0
        print(max(A))
