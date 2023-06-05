def func():
    #N, X = map(int, input().split())
    #S = input()
    N, X = 3, 0
    S = 'xox'
    score = X
    for s in S:
        if s == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    print(score)
