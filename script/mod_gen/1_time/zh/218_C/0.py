def match_str(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

if __name__ == '__main__':
    match_str()