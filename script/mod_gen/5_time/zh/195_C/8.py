def count_commas(number):
    if number < 1000:
        return 0
    else:
        return int(number / 1000) + count_commas(int(number/1000))

if __name__ == '__main__':
    count_commas()