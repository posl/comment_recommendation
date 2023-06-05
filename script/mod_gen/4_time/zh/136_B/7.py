def count_odd(n):
    count = 0
    for i in range(1,n+1):
        if i < 10:
            count += 1
        else:
            if i % 2 != 0:
                count += 1
    return count

if __name__ == '__main__':
    count_odd()