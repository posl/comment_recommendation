def main():
    n,x = map(int,input().split())
    s = input()
    score = x
    for i in s:
        if i == 'o':
            score += 1
        else:
            if score == 0:
                continue
            else:
                score -= 1
    print(score)
