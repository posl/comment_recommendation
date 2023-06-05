def isMatch(string1,string2):
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)):
        if string1[i] != string2[i] and string2[i] != '_':
            return False
    return True
