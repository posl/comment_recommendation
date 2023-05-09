def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        if A[i] > 10:
            sum += A[i] - 10
    print(sum)
