def max_sum(n,m,a):
    sum = 0
    for i in range(1,m+1):
        sum += i * a[i-1]
    return sum

if __name__ == '__main__':
    max_sum()