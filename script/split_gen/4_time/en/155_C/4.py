def countVotes(votes):
    votesCount = {}
    for vote in votes:
        if vote in votesCount:
            votesCount[vote] += 1
        else:
            votesCount[vote] = 1
    return votesCount
