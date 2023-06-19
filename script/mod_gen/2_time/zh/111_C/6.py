def find_min_change_num(n, v):
    min_change_num = n
    for i in range(2):
        cnt = 0
        for j in range(i, n, 2):
            if v[j] != v[i]:
                cnt += 1
        min_change_num = min(min_change_num, cnt)
    return min_change_num

if __name__ == '__main__':
    find_min_change_num()