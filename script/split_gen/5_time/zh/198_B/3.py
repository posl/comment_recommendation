def isPalindrome(num):
    num_str = str(num)
    num_str_reverse = num_str[::-1]
    if num_str == num_str_reverse:
        return True
    else:
        return False
