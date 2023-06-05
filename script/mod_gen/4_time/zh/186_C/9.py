def count7(n):
    count = 0
    for i in range(n+1):
        if '7' in str(i) or '7' in oct(i):
            count += 1
    return count

if __name__ == '__main__':
    count7()