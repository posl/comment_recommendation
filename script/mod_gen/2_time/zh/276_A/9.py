def find_last_index(s, c):
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            index = i + 1
    return index

if __name__ == '__main__':
    find_last_index()