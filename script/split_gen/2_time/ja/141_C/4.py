def main():
    N, K, Q = map(int, input().split())
    scores = [K for _ in range(N)]
    for _ in range(Q):
        scores[int(input()) - 1] += 1
    for score in scores:
        print("Yes" if score > Q else "No")
