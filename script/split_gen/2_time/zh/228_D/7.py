def main():
    N, K = map(int, input().split())
    scores = []
    for _ in range(N):
        scores.append(sum(map(int, input().split())))
    scores.sort(reverse=True)
    print('Yes' if scores[K-1] > scores[K] else 'No')
