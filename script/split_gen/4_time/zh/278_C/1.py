def find(a):
    if a not in dic:
        dic[a] = a
        return a
    if dic[a] == a:
        return a
    else:
        dic[a] = find(dic[a])
        return dic[a]
