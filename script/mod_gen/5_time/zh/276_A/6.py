def last_index(s):
    index = -1
    for i in range(len(s)):
        if s[i] == "a":
            index = i
    return index + 1

if __name__ == '__main__':
    last_index()