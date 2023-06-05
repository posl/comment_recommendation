def follow(a,b):
    if a in follow_dict.keys():
        follow_dict[a].append(b)
    else:
        follow_dict[a] = [b]
    if b in followed_dict.keys():
        followed_dict[b].append(a)
    else:
        followed_dict[b] = [a]
