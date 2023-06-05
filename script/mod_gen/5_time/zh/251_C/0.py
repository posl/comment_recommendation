def find_best_submission(n, submissions):
    best_score = 0
    best_index = 0
    best_submission = ''
    for i in range(n):
        submission = submissions[i][0]
        score = submissions[i][1]
        if score > best_score:
            best_score = score
            best_index = i
            best_submission = submission
        elif score == best_score:
            if submission < best_submission:
                best_score = score
                best_index = i
                best_submission = submission
    return best_index + 1

if __name__ == '__main__':
    find_best_submission()