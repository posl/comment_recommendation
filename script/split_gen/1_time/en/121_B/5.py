def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        if sum([a*b for a, b in zip(A[i], B)])+C > 0:
            cnt += 1
    print(cnt)
