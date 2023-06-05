def count_odd_digits(n):
    count = 0
    for i in range(1,n+1):
        if i < 10:
            if i % 2 == 1:
                count += 1
        elif i < 100:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 2 == 1:
                count += 1
        elif i < 1000:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 10 % 2 == 1:
                count += 1
            if i // 100 % 2 == 1:
                count += 1
        elif i < 10000:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 10 % 2 == 1:
                count += 1
            if i // 100 % 10 % 2 == 1:
                count += 1
            if i // 1000 % 2 == 1:
                count += 1
        elif i < 100000:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 10 % 2 == 1:
                count += 1
            if i // 100 % 10 % 2 == 1:
                count += 1
            if i // 1000 % 10 % 2 == 1:
                count += 1
            if i // 10000 % 2 == 1:
                count += 1
        else:
            if i % 10 % 2 == 1:
                count += 1
            if i // 10 % 10 % 2 == 1:
                count += 1
            if i // 100 % 10 % 2 == 1:
                count += 1
            if i // 1000 % 10 % 2 == 1:
                count += 1
            if i // 10000 % 10 % 2 == 1:
                count += 1
            if i // 100000 % 2 == 1:
                count += 1
    return count
n

if __name__ == '__main__':
    count_odd_digits()