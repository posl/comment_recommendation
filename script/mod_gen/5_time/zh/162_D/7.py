def find_next_char(s, i, c):
    for j in range(i+1, len(s)):
        if s[j] != c:
            return j
    return -1

if __name__ == '__main__':
    find_next_char()