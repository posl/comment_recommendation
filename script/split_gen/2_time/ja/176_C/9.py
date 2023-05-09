def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    result = 0
    for i in range(N):
        if A[i] > A[i+1]:
            result += A[i] - A[i+1]
            A[i] = A[i+1]
    print(result)
