def merge(s):
    if len(s) == 1:
        return 1
    if s[0] == s[1]:
        return merge(s[1:])
    else:
        return 1 + merge(s[1:])

if __name__ == '__main__':
    merge()