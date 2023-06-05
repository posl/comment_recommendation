def solve():
    N, X = map(int, input().split())
    S = input()
    score = X
    for s in S:
        if s == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    print(score)
