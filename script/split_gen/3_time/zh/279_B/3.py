def check_substring(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    if len1 < len2:
        return False
    if len1 == len2:
        if string1 == string2:
            return True
        else:
            return False
    for i in range(len1-len2+1):
        if string1[i:i+len2] == string2:
            return True
    return False
