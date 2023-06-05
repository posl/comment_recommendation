def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    like = [0] * M
    for i in range(N):
        for j in range(A[i][0]):
            like[A[i][j+1]-1] += 1
    print(like.count(N))
