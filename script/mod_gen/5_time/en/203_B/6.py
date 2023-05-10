def calc_sum(n, k):
    total_sum = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            total_sum += int(str(i) + str(j) + str(0))
    return total_sum

if __name__ == '__main__':
    calc_sum()