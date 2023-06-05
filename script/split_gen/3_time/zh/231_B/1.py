def get_max_vote(candidates):
    max_vote = 0
    max_vote_name = ""
    for candidate in candidates:
        if candidates[candidate] > max_vote:
            max_vote = candidates[candidate]
            max_vote_name = candidate
    return max_vote_name
