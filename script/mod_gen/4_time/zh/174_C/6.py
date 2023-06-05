def get_num(k):
    if k % 2 == 0 or k % 5 == 0:
        return -1
    else:
        num = 0
        for i in range(1, k + 1):
            num = (num * 10 + 7) % k
            if num == 0:
                return i
        return -1

if __name__ == '__main__':
    get_num()