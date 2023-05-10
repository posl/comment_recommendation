def main():
    N, K = map(int, input().split())
    scores = []
    for i in range(N):
        scores.append(list(map(int, input().split())))
    for i in range(N):
        if scores[i][0] + scores[i][1] + scores[i][2] >= 300 * 3 - K:
            print("Yes")
        else:
            print("No")
