def solution(a, n):
    if a == 1:
        return n - 1
    if a == n:
        return 1
    if a > n:
        return -1
    # find the number of digits in n
    num_digits = len(str(n))
    # find the number of digits in a
    num_digits_a = len(str(a))
    if num_digits_a > num_digits:
        return -1
    # find the number of digits in a^n
    num_digits_a_n = len(str(a ** num_digits))
    if num_digits_a_n > num_digits:
        return -1
    # find the number of times we need to multiply a to get n
    num_times = num_digits - num_digits_a_n
    # check if we can do it in less than num_times + 1
    if num_times + 1 < num_digits:
        return num_times + 1
    else:
        return -1

if __name__ == '__main__':
    solution()