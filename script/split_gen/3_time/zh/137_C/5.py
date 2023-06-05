def get_hash(s):
    hash = [0]*26
    for c in s:
        hash[ord(c)-ord('a')] += 1
    return hash
