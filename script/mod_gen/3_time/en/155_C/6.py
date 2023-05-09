def main():
    n = int(input())
    votes = []
    for i in range(n):
        votes.append(input())
    votes.sort()
    count = 0
    max_count = 0
    max_votes = []
    for i in range(n):
        if i == 0:
            count += 1
            continue
        if votes[i] == votes[i-1]:
            count += 1
        else:
            if max_count < count:
                max_count = count
                max_votes = []
                max_votes.append(votes[i-1])
            elif max_count == count:
                max_votes.append(votes[i-1])
            count = 1
    if max_count < count:
        max_count = count
        max_votes = []
        max_votes.append(votes[n-1])
    elif max_count == count:
        max_votes.append(votes[n-1])
    for vote in max_votes:
        print(vote)
    return

if __name__ == '__main__':
    main()