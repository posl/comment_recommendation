def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [-1] * N
    for i in range(N):
        B[A[i]-1] = i+1
    print(*B)
