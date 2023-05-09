def replace_comma(str):
    count = 0
    new_str = ""
    for i in str:
        if i == '"':
            count += 1
        elif i == ',' and count % 2 == 0:
            new_str += '.'
        else:
            new_str += i
    return new_str

if __name__ == '__main__':
    replace_comma()