def get_odd_num(n):
    if n < 10:
        return n
    else:
        odd_num = 9
        for i in range(10, n+1):
            if i % 2 == 1:
                odd_num += 1
        return odd_num

if __name__ == '__main__':
    get_odd_num()