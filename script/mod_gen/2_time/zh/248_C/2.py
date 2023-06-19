def get_count(n, m, k):
    if n == 1:
        if m >= k:
            return 1
        else:
            return 0
    else:
        count = 0
        for i in range(1, m+1):
            count += get_count(n-1, m, k-i)
        return count

if __name__ == '__main__':
    get_count()