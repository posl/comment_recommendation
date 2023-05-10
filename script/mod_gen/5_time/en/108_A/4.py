def count_pairs(number):
    count = 0
    for i in range(1, number+1):
        if i % 2 == 0:
            continue
        for j in range(1, number+1):
            if j % 2 == 1:
                continue
            count += 1
    return count
print(count_pairs(int(input())))

if __name__ == '__main__':
    count_pairs()