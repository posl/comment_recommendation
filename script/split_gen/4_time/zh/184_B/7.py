def main():
    N,X = [int(x) for x in input().split()]
    S = input()
    score = X
    for c in S:
        if c == 'o':
            score += 1
        elif c == 'x' and score > 0:
            score -= 1
    print(score)
