def check_follow(a, b, follows):
    if a in follows[b] and b in follows[a]:
        return True
    else:
        return False
