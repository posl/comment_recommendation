def rating(a):
    if a < 1200:
        return "ABC"
    elif a < 2800:
        return "ARC"
    else:
        return "AGC"

if __name__ == '__main__':
    rating()