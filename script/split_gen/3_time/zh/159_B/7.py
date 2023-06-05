def judege_palindrome(str):
    str_len = len(str)
    if str_len % 2 == 0:
        return False
    else:
        for i in range(0, (str_len - 1) // 2):
            if str[i] != str[str_len - 1 - i]:
                return False
        return True
