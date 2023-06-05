def get_max_books(n, m, k, a, b):
    if n + m > k:
        return 0
    else:
        a_sum = 0
        b_sum = 0
        count = 0
        while a_sum + b_sum < k:
            if a_sum + a[count] < b_sum + b[count]:
                a_sum += a[count]
                count += 1
                if count == n:
                    return count
            else:
                b_sum += b[count]
                count += 1
                if count == m:
                    return count
        return count

if __name__ == '__main__':
    get_max_books()