def find_kth(a, x, k):
    cnt = 0
    for i in range(len(a)):
        if a[i] == x:
            cnt += 1
            if cnt == k:
                return i+1
    return -1

if __name__ == '__main__':
    find_kth()