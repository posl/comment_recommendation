def follow(a,b):
    if a in follow_dic:
        if b in follow_dic[a]:
            return True
    return False
