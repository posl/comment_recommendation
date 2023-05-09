def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    sum = 0
    for i in range(N):
        sum += A[i] * i - A[i] * (N - 1 - i)
    print(sum)
