def count_commas(num):
    if num < 1000:
        return 0
    else:
        return count_commas(num/1000) + 1

if __name__ == '__main__':
    count_commas()