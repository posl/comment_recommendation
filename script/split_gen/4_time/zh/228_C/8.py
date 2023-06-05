def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: sum(x), reverse=True)
    for i in range(N):
        if sum(P[i]) > sum(P[K - 1]):
            print('Yes')
        else:
            print('No')
