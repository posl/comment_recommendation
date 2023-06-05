def find_miss_num(s):
    numbers = list(range(10))
    for i in range(len(s)):
        numbers.remove(int(s[i]))
    return numbers[0]

if __name__ == '__main__':
    find_miss_num()