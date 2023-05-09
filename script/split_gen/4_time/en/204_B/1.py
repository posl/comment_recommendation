def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(N):
        if A[i] > 10:
            result += A[i] - 10
    print(result)
