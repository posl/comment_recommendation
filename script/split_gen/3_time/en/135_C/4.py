def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    for i in range(N):
        if A[i] <= B[i]:
            result += A[i]
            B[i] -= A[i]
            if A[i+1] <= B[i]:
                result += A[i+1]
                A[i+1] = 0
            else:
                result += B[i]
                A[i+1] -= B[i]
        else:
            result += B[i]
    print(result)
