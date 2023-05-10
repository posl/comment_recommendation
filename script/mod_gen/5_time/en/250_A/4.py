def get_adjacent_count(h, w, r, c):
    count = 0
    if r > 1:
        count += 1
    if r < h:
        count += 1
    if c > 1:
        count += 1
    if c < w:
        count += 1
    return count

if __name__ == '__main__':
    get_adjacent_count()