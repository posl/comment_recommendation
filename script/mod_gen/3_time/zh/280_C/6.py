def find_diff(s, t):
    for i in range(len(t)):
        if s[i] != t[i]:
            return i
    return len(t)

if __name__ == '__main__':
    find_diff()