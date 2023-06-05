def get_comma_count(num):
    comma_count = 0
    num_len = len(str(num))
    if num_len <= 3:
        return 0
    else:
        for i in range(1, num_len - 1):
            if i % 3 == 0:
                comma_count += 1
        return comma_count
