def find_second_lowest_score(scores):
    scores = sorted(scores)
    second_lowest_score = scores[1]
    for i in range(2, len(scores)):
        if scores[i] > second_lowest_score:
            return scores[i]

if __name__ == '__main__':
    find_second_lowest_score()