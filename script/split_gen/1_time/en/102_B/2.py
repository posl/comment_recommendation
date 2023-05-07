def main():
    N = int(input())
    A = list(map(int, input().split()))
    min = A[0]
    max = A[0]
    for i in range(1, N):
        if A[i] < min:
            min = A[i]
        elif A[i] > max:
            max = A[i]
    print(max - min)
