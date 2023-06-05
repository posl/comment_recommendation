def get_kth(k):
    i = 0
    while k > 0:
        i += 1
        if '2' not in str(i):
            k -= 1
    return i

if __name__ == '__main__':
    get_kth()