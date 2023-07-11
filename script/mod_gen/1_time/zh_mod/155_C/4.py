def most_common(lst):
    return max(set(lst), key=lst.count)

if __name__ == '__main__':
    most_common()