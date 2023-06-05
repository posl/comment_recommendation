def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A = A + A
    sum = 0
    for i in range(N):
        sum += A[i]
    max = sum
    for i in range(N):
        sum -= A[i]
        sum += A[i+N//2]
        if sum > max:
            max = sum
    print(max)
