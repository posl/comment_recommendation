def main():
    N,M = map(int,input().split())
    friend_list = [list(map(int,input().split())) for _ in range(M)]
    friend_dict = {i:[] for i in range(1,N+1)}
    for a,b in friend_list:
        friend_dict[a].append(b)
        friend_dict[b].append(a)
    group_list = []
    for i in range(1,N+1):
        if i in group_list:
            continue
        group = [i]
        group_list.append(i)
        while len(group) > 0:
            group = list(set(group))
            friend = []
            for j in group:
                friend += friend_dict[j]
            friend = list(set(friend))
            friend = [i for i in friend if i not in group_list]
            group_list += friend
            group = friend
    print(len(group_list))
