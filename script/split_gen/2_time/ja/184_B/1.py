def main():
    n, x = map(int, input().split())
    s = input()
    score = x
    for i in range(n):
        if s[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    print(score)
