def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(4*N-1):
        B[A[i]-1] += 1
    for i in range(N):
        if B[i] % 2 == 1:
            print(i+1)
            exit(0)
