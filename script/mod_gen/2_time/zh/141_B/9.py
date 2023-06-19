def is_easy_dance(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                return False
        else:
            if s[i] == 'R':
                return False
    return True

if __name__ == '__main__':
    is_easy_dance()