def find_good_integers(w):
    if w <= 2:
        return [1, 2]
    elif w == 3:
        return [1, 2, 3]
    else:
        return [1, 2, 3] * (w // 3) + [1, 2, 3][:w % 3]

if __name__ == '__main__':
    find_good_integers()