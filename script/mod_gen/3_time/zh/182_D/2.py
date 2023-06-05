def max_coor(n, a):
    max = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > max:
            max = sum
    return max

if __name__ == '__main__':
    max_coor()