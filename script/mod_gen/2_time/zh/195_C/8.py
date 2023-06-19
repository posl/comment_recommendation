def count_comma(num):
    count = 0
    num = str(num)
    num_len = len(num)
    if num_len <= 3:
        return 0
    else:
        for i in range(1, num_len):
            if i % 3 == 0:
                count += 1
    return count

if __name__ == '__main__':
    count_comma()