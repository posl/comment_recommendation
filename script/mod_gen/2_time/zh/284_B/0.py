def odd_num(a):
    count = 0
    for i in a:
        if i%2 != 0:
            count += 1
    return count

if __name__ == '__main__':
    odd_num()