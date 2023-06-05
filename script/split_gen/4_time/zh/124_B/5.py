def get_sea_view_count(h):
    count = 0
    for i in range(len(h)):
        if i == 0:
            count += 1
        else:
            if h[i] >= max(h[0:i]):
                count += 1
    return count
