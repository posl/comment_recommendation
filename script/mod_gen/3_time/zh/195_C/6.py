def get_comma_count(n):
    comma_count = 0
    num_str = str(n)
    num_len = len(num_str)
    if num_len <= 3:
        return 0
    else:
        if num_len % 3 == 0:
            comma_count = num_len // 3 - 1
        else:
            comma_count = num_len // 3
        return comma_count

if __name__ == '__main__':
    get_comma_count()