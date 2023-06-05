def find_miss_num(s):
    numbers = list(range(10))
    for i in range(len(s)):
        numbers.remove(int(s[i]))
    return numbers[0]
