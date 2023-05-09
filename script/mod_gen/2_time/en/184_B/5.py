def answer(N, X, S):
    points = X
    for i in range(N):
        if S[i] == 'o':
            points += 1
        else:
            if points > 0:
                points -= 1
    return points

if __name__ == '__main__':
    answer()