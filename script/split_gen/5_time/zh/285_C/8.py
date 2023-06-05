def get_index(s):
    index = 0
    for i in range(len(s)):
        index += (ord(s[i])-ord('A')+1)*(26**(len(s)-i-1))
    return index
