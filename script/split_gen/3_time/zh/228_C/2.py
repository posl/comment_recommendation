def solve():
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores.sort(key=lambda x: sum(x), reverse=True)
    scores = scores[:K]
    scores.sort(key=lambda x: x[0], reverse=True)
    scores = scores[:K]
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[:K]
    scores.sort(key=lambda x: x[2], reverse=True)
    scores = scores[:K]
    for i in range(N):
        if scores.count(scores[i]) > 0:
            print("Yes")
        else:
            print("No")
