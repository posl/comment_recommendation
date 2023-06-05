def last_index_of_a(s):
    index = -1
    for i in range(len(s)):
        if s[i] == 'a':
            index = i + 1
    return index

if __name__ == '__main__':
    last_index_of_a()