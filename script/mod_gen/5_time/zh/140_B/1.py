def get_score(n, dish, satisfaction, bonus):
    score = 0
    for i in range(n):
        score += satisfaction[dish[i]-1]
        if i < n-1 and dish[i] == dish[i+1]-1:
            score += bonus[dish[i]-1]
    return score

if __name__ == '__main__':
    get_score()