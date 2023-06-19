def get_max_vote_name():
    n = int(input())
    name_list = []
    vote_list = []
    for i in range(n):
        name = input()
        if name not in name_list:
            name_list.append(name)
            vote_list.append(1)
        else:
            vote_list[name_list.index(name)] += 1
    return name_list[vote_list.index(max(vote_list))]

if __name__ == '__main__':
    get_max_vote_name()