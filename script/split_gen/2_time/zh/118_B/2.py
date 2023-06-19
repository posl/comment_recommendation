def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]
    #print(N, M, A)
    # 与えられたN人のうち、全員が好きな食べ物の数を数える
    # 食べ物の数を数える
    # 食べ物を数える
    #print(A)
    like = [0] * M
    for i in range(N):
        for j in range(len(A[i])):
            like[A[i][j]-1] += 1
    #print(like)
    cnt = 0
    for i in range(M):
        if like[i] == N:
            cnt += 1
    print(cnt)
