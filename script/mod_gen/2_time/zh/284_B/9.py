def count_odd_num(num_list):
    count = 0
    for i in num_list:
        if i % 2 != 0:
            count += 1
    return count

if __name__ == '__main__':
    count_odd_num()