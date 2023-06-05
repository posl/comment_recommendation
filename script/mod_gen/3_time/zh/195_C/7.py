def comma_count(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 1000
    return count - 1
n = int(input())

if __name__ == '__main__':
    comma_count()