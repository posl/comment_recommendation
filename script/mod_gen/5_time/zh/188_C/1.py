def findSecondMaxScore(scores):
    scores = sorted(scores)
    return scores[-2]

if __name__ == '__main__':
    findSecondMaxScore()