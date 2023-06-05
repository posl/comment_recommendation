def follow(a, b):
    if a in following[b] and b in following[a]:
        return True
    else:
        return False
