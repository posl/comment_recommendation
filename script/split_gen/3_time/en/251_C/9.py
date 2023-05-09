def main():
    n = int(input())
    scores = []
    for _ in range(n):
        s, t = input().split()
        scores.append((s, int(t)))
    best_score = 0
    best_score_index = 0
    for i, (s, t) in enumerate(scores):
        if t > best_score and s not in [s for s, _ in scores[:i]]:
            best_score = t
            best_score_index = i
    print(best_score_index + 1)
