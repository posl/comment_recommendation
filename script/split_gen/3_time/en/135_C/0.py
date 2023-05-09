def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    result = 0
    for i in range(N):
        if A[i] <= B[i]:
            result += A[i]
            if A[i+1] <= B[i] - A[i]:
                result += A[i+1]
                A[i+1] = 0
            else:
                result += B[i] - A[i]
                A[i+1] -= B[i] - A[i]
        else:
            result += B[i]
    print(result + min(A[-1], B[-1]))
