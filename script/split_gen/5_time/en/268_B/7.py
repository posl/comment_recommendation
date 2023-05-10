def is_prefix(str1, str2):
    if str1 == str2[:len(str1)]:
        return True
    else:
        return False
