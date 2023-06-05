def is_contain_seven(x):
    return x % 10 == 7 or x // 10 % 10 == 7 or x // 100 % 10 == 7
