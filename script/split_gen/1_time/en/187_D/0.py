def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort(reverse=True)
    B.sort(reverse=True)
    Aoki = 0
    Takahashi = 0
    for i in range(N):
        Aoki += A[i]
        Takahashi += B[i]
        if Aoki < Takahashi:
            print(i + 1)
            return
    print(N)
