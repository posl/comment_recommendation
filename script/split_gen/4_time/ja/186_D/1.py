def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N-1):
        sum += A[i+1] - A[i]
    print(sum * (N-1) - sum * (N-1) // 2 * 2)
