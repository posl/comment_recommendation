def main():
    N, K = map(int, input().split())
    scores = [0] * N
    for i in range(N):
        scores[i] = sum(map(int, input().split()))
    scores.sort(reverse=True)
    print("Yes" if scores[K - 1] > 0 else "No")
