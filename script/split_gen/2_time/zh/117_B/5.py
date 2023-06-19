def is_polygon(L):
    max_length = max(L)
    if max_length < sum(L)-max_length:
        return True
    else:
        return False
