def single_char(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
    return -1

if __name__ == '__main__':
    single_char()