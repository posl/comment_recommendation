def get_max_vote_name():
    n = int(input())
    vote_dict = {}
    for i in range(n):
        name = input()
        if name in vote_dict:
            vote_dict[name] += 1
        else:
            vote_dict[name] = 1
    max_vote = 0
    max_name = ''
    for k, v in vote_dict.items():
        if v > max_vote:
            max_vote = v
            max_name = k
    print(max_name)
get_max_vote_name()
