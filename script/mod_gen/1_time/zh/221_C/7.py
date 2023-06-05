def get_max_product(num):
    if num < 10:
        return 0
    if num < 100:
        return num
    if num < 1000:
        return int(str(num)[0]) * int(str(num)[1:])
    if num < 10000:
        return int(str(num)[0:2]) * int(str(num)[2:])
    if num < 100000:
        return int(str(num)[0:2]) * int(str(num)[2:])
    if num < 1000000:
        return int(str(num)[0:3]) * int(str(num)[3:])
    if num < 10000000:
        return int(str(num)[0:3]) * int(str(num)[3:])
    if num < 100000000:
        return int(str(num)[0:4]) * int(str(num)[4:])
    if num < 1000000000:
        return int(str(num)[0:4]) * int(str(num)[4:])

if __name__ == '__main__':
    get_max_product()