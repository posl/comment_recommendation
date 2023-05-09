def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    total = 0
    for i in range(N):
        if A[i] <= B[i]:
            total += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                total += A[i+1]
                B[i] -= A[i+1]
            else:
                total += B[i]
                A[i+1] -= B[i]
        else:
            total += B[i]
    print(total)
