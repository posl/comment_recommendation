def count7(n):
    count = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    return count

if __name__ == '__main__':
    count7()