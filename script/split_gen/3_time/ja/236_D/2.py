def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    B = [0]*N
    for i in range(N):
        for j in range(2*N-1):
            B[i] ^= A[j][i]
    print(*B)
