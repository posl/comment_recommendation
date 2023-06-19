def move(s, k):
    l = len(s)
    ret = ''
    for i in range(l):
        ret += chr((ord(s[i]) - ord('a') + k) % 26 + ord('a'))
    return ret

if __name__ == '__main__':
    move()