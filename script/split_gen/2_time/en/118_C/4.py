def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    H = [0] * N
    H[0] = A[0]
    for i in range(1, N):
        H[i] = max(0, A[i] - H[i-1])
    print(H[-1])
