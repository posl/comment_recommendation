def is_easy_to_play(s):
    if len(s) == 0:
        return False
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                return False
        else:
            if s[i] == 'R':
                return False
    return True

if __name__ == '__main__':
    is_easy_to_play()