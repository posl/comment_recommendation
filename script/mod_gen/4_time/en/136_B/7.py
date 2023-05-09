def count_odd_digits(n):
    # 1桁の場合
    if n < 10:
        return 1
    # 2桁以上の場合
    count = 9
    for i in range(10, n + 1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

if __name__ == '__main__':
    count_odd_digits()