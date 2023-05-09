def check_substring(s, t):
    i = 0
    while i < len(s):
        if s[i:i+len(t)] == t:
            return True
        i += 1
    return False

if __name__ == '__main__':
    check_substring()