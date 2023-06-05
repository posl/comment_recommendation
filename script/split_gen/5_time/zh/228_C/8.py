def main():
    n, k = map(int, input().split())
    score = []
    for i in range(n):
        score.append(sum(list(map(int, input().split()))))
    score.sort(reverse=True)
    print("Yes" if score[k-1] > score[k] else "No")
