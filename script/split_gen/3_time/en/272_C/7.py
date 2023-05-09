def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 1000000001
    for i in range(N):
        B[A[i]] = 1
    for i in range(N):
        for j in range(i+1, N):
            if B[A[i] + A[j]] == 1:
                B[A[i] + A[j]] = 2
    for i in range(1000000000, -1, -2):
        if B[i] == 2:
            print(i)
            return
    print(-1)
