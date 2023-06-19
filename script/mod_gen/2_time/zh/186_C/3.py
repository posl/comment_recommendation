def count_num(n):
    count = 0
    for i in range(1, n + 1):
        if '7' in str(i) or '7' in oct(i):
            pass
        else:
            count += 1
    return count

if __name__ == '__main__':
    count_num()