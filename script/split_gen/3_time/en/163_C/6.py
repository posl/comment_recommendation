def main():
    N = int(input())
    A = list(map(int, input().split()))
    subordinates = [0] * N
    for i in range(1, N):
        subordinates[A[i-1]-1] += 1
    for i in range(N):
        print(subordinates[i])
