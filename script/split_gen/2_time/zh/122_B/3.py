def get_length(s):
    length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_acgt(s[i:j]):
                length = max(length, j-i)
    return length
