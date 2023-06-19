def get_max_vote_name(names):
    max_vote_name = ""
    max_vote_count = 0
    for name in names:
        vote_count = names.count(name)
        if vote_count > max_vote_count:
            max_vote_count = vote_count
            max_vote_name = name
    return max_vote_name
