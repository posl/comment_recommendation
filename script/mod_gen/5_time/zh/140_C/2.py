def max_sum(a):
    sum = 0
    for i in range(len(a)):
        if i == 0:
            sum += a[i]
        else:
            sum += max(a[i-1], a[i])
    return sum

if __name__ == '__main__':
    max_sum()