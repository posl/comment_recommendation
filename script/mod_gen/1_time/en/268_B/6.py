def is_prefix(str1, str2):
    if str1[0:len(str1)] == str2[0:len(str1)]:
        return True
    else:
        return False

if __name__ == '__main__':
    is_prefix()