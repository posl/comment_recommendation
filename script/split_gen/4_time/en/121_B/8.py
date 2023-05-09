def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    answer = 0
    for i in range(N):
        score = 0
        for j in range(M):
            score += A[i][j] * B[j]
        if score + C > 0:
            answer += 1
    print(answer)
