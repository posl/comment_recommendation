def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        A[i] = list(map(int, input().split()))
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum + C > 0:
            count += 1
    print(count)
