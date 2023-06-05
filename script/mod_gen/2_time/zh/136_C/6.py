def odd_number(n):
    count = 0
    for i in range(1,n+1):
        if i < 10:
            if i % 2 == 1:
                count += 1
        elif i < 100:
            if i % 2 == 1:
                count += 1
        elif i < 1000:
            if i % 2 == 1:
                count += 2
        elif i < 10000:
            if i % 2 == 1:
                count += 2
        elif i < 100000:
            if i % 2 == 1:
                count += 3
        elif i < 1000000:
            if i % 2 == 1:
                count += 3
        elif i < 10000000:
            if i % 2 == 1:
                count += 4
        elif i < 100000000:
            if i % 2 == 1:
                count += 4
        elif i < 1000000000:
            if i % 2 == 1:
                count += 5
        elif i < 10000000000:
            if i % 2 == 1:
                count += 5
    return count

if __name__ == '__main__':
    odd_number()