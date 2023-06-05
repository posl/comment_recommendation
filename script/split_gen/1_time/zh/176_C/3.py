def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = A[0]
    sum = 0
    for i in range(1, N):
        if A[i] > max:
            max = A[i]
        else:
            sum += max - A[i]
    print(sum)
