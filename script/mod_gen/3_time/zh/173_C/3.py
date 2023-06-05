def count_black(s):
    return sum([1 if c == '#' else 0 for c in s])

if __name__ == '__main__':
    count_black()