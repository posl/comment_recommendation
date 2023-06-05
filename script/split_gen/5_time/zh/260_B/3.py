def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    scores = []
    for i in range(N):
        scores.append((A[i], B[i], i + 1))
    scores.sort(reverse=True)
    scores = scores[:X + Y + Z]
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[:Y + Z]
    scores.sort(key=lambda x: x[0] + x[1], reverse=True)
    scores = scores[:Z]
    scores.sort(key=lambda x: x[2])
    for score in scores:
        print(score[2])
