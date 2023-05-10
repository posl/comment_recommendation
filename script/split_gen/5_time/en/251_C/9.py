def get_best_submission(submissions):
    submissions.sort(key=lambda x: x[1], reverse=True)
    return submissions[0][0]
