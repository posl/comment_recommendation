def getHash(s):
    hash = [0] * 26
    for i in range(len(s)):
        hash[ord(s[i]) - ord('a')] += 1
    return hash

if __name__ == '__main__':
    getHash()