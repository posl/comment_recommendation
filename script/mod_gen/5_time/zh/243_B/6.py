def get_same_num(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
    return cnt

if __name__ == '__main__':
    get_same_num()