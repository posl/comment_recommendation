def find_value(a, x, k):
    result = -1
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
            if count == k:
                result = i + 1
                break
    return result

if __name__ == '__main__':
    find_value()