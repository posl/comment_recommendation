def easy_to_play(s):
    for i in range(len(s)):
        if (i+1)%2 == 1:
            if s[i] not in ['R','U','D']:
                return False
        else:
            if s[i] not in ['L','U','D']:
                return False
    return True

if __name__ == '__main__':
    easy_to_play()