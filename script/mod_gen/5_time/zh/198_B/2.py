def isPalindrome(num):
    num_list = list(str(num))
    num_list.reverse()
    num_reverse = int(''.join(num_list))
    if num_reverse == num:
        return True
    else:
        return False

if __name__ == '__main__':
    isPalindrome()