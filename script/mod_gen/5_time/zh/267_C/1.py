def get_max_sum(n, m, a):
    #print("n: %d, m: %d" % (n, m))
    #print(a)
    max_sum = 0
    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += (j+1)*a[i+j]
        if sum > max_sum:
            max_sum = sum
    return max_sum

if __name__ == '__main__':
    get_max_sum()