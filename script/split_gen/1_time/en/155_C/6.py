def main():
    N = int(input())
    votes = [input() for _ in range(N)]
    votes.sort()
    candidates = []
    max_vote = 0
    for i in range(N):
        if i == 0:
            candidate = votes[i]
            vote = 1
        else:
            if candidate == votes[i]:
                vote += 1
            else:
                if vote > max_vote:
                    candidates = [candidate]
                    max_vote = vote
                elif vote == max_vote:
                    candidates.append(candidate)
                candidate = votes[i]
                vote = 1
    if vote > max_vote:
        candidates = [candidate]
        max_vote = vote
    elif vote == max_vote:
        candidates.append(candidate)
    candidates.sort()
    for candidate in candidates:
        print(candidate)
