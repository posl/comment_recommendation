def is_double_copy_string(string):
    string_len = len(string)
    if string_len % 2 != 0:
        return False
    else:
        string_half_len = int(string_len / 2)
        if string[0:string_half_len] == string[string_half_len:]:
            return True
        else:
            return False

if __name__ == '__main__':
    is_double_copy_string()