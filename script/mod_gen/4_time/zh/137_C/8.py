def get_hash(s):
    hash = 0
    for i in range(0, len(s)):
        hash += ord(s[i]) * pow(10, i)
    return hash

if __name__ == '__main__':
    get_hash()