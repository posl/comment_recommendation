def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    max_vote = 0
    vote_dict = {}
    for s in S:
        if s in vote_dict:
            vote_dict[s] += 1
        else:
            vote_dict[s] = 1
        max_vote = max(max_vote, vote_dict[s])
    for s in S:
        if vote_dict[s] == max_vote:
            print(s)

if __name__ == '__main__':
    main()