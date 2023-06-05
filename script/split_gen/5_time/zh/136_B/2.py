def count_odd(n):
    count = 0
    for i in range(1, n + 1):
        if i < 10:
            if i % 2 != 0:
                count += 1
        else:
            if i % 2 != 0:
                count += 1
            else:
                for j in range(1, len(str(i))):
                    if int(str(i)[j]) % 2 != 0:
                        count += 1
                        break
    return count
print(count_odd(100000))
