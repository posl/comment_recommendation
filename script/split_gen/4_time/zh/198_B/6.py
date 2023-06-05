def is_palindrome(num):
    num_str = str(num)
    num_str_len = len(num_str)
    if num_str_len == 1:
        return True
    elif num_str_len == 2:
        return True if num_str[0] == num_str[1] else False
    else:
        if num_str[0] == num_str[num_str_len - 1]:
            return is_palindrome(num_str[1:num_str_len - 1])
        else:
            return False
