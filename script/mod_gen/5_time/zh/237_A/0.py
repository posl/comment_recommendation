def is_in_range(n):
    if -2**31 <= n <= 2**31-1:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    is_in_range()