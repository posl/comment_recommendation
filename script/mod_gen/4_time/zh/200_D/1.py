def find_sum_equal_200(n, a):
    m = len(a)
    for i in range(m):
        for j in range(i+1, m):
            if (a[i]+a[j])%200 == 0:
                return True, [i+1], [j+1]
    return False, [], []

if __name__ == '__main__':
    find_sum_equal_200()