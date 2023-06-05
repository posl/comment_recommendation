def get_min_element(start, end, a):
    min_element = 100000
    for i in range(start, end + 1):
        if a[i] < min_element:
            min_element = a[i]
    return min_element

if __name__ == '__main__':
    get_min_element()