def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K-Q for _ in range(N)]
    for a in A:
        score[a-1] += 1
    for s in score:
        if s > 0:
            print('Yes')
        else:
            print('No')
