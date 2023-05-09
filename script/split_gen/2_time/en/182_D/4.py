def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum > max:
            max = sum
    print(max)
