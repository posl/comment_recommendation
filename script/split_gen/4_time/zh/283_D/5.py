def is_good_str(str):
    while True:
        if str.find('()') == -1:
            break
        str = str.replace('()','')
    return str == ''
