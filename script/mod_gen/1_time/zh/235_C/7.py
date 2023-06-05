def get_answer(a, x, k):
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
            if count == k:
                return i+1
    return -1

if __name__ == '__main__':
    get_answer()