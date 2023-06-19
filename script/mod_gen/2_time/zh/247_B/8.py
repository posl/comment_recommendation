def get_nickname(s, t):
    for i in range(len(s)):
        if s[i] == t[i]:
            return s[i]
    return ""

if __name__ == '__main__':
    get_nickname()