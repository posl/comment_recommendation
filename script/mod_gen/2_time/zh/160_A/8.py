def count_pairs(n, a):
    cnt = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            if a[i-1] == a[j-1]:
                cnt += 1
    return cnt

if __name__ == '__main__':
    count_pairs()