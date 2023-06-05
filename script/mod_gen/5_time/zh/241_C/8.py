def is_ok(s):
    for i in range(len(s)):
        if s[i] == "#":
            return False
    return True

if __name__ == '__main__':
    is_ok()