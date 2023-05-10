def check_good_string(str):
    if str == "":
        return True
    elif str[0] == ")" or str[-1] == "(":
        return False
    else:
        return check_good_string(str[1:-1])

if __name__ == '__main__':
    check_good_string()