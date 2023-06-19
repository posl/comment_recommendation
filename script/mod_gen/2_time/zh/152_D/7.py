def get_num(n):
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        elif i < 100:
            if i % 11 == 0:
                count += 1
            else:
                count += 2
        elif i < 1000:
            if i % 11 == 0:
                count += 1
            else:
                count += 3
        elif i < 10000:
            if i % 11 == 0:
                count += 1
            else:
                count += 4
        elif i < 100000:
            if i % 11 == 0:
                count += 1
            else:
                count += 5
        elif i < 1000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 6
        elif i < 10000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 7
        elif i < 100000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 8
        elif i < 1000000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 9
        elif i < 10000000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 10
        else:
            if i % 11 == 0:
                count += 1
            else:
                count += 11
    return count

if __name__ == '__main__':
    get_num()