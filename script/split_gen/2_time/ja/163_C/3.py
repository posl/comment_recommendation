def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = [0] * N
    for i in range(N-1):
        C[A[i]-1] += 1
    for c in C:
        print(c)
