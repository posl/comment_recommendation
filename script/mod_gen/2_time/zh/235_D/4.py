def get_index(A, x, k):
    i = 0
    count = 0
    for a in A:
        if a == x:
            count += 1
            if count == k:
                return i + 1
        i += 1
    return -1

if __name__ == '__main__':
    get_index()