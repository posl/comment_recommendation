def main():
    n, k = map(int, input().split())
    scores = []
    for i in range(n):
        scores.append(list(map(int, input().split())))
    print(scores)
    for i in range(n):
        scores[i].sort(reverse=True)
        if scores[i][0] + scores[i][1] + scores[i][2] >= k:
            print("Yes")
        else:
            print("No")
