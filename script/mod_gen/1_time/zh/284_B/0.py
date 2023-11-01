def count_odd(a):
    count = 0
    for i in a:
        if i % 2 == 1:
            count += 1
    return count

if __name__ == '__main__':
    count_odd()