def main():
    n, k = map(int, input().split())
    score = []
    for i in range(n):
        score.append(list(map(int, input().split())))
    for i in range(n):
        score[i].sort(reverse=True)
    for i in range(n):
        if score[i][0] + score[i][1] + score[i][2] >= k:
            print("Yes")
        else:
            print("No")
