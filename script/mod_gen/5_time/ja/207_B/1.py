def count_operation(a,b,c,d):
    if a <= b:
        return -1
    if b > c*d:
        return 0
    count = 0
    while True:
        if a <= b:
            break
        a += c
        b += d
        count += 1
    return count

if __name__ == '__main__':
    count_operation()