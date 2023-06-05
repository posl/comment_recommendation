def count_group(n, m, friends):
    group = [0] * n
    groups = []
    group_id = 1
    for friend in friends:
        friend1 = friend[0] - 1
        friend2 = friend[1] - 1
        if group[friend1] == 0 and group[friend2] == 0:
            group[friend1] = group_id
            group[friend2] = group_id
            groups.append(group_id)
            group_id += 1
        elif group[friend1] != 0 and group[friend2] == 0:
            group[friend2] = group[friend1]
        elif group[friend1] == 0 and group[friend2] != 0:
            group[friend1] = group[friend2]
        else:
            if group[friend1] != group[friend2]:
                for i in range(n):
                    if group[i] == group[friend2]:
                        group[i] = group[friend1]
                groups.remove(group[friend2])
    return len(groups) + n - sum(group)
