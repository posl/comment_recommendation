def move(s, k):
    for i in range(len(s)):
        if s[i] == "z":
            s[i] = "a"
        else:
            s[i] = chr(ord(s[i]) + k)
    return s

if __name__ == '__main__':
    move()