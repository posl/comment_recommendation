def find_subordinates(n, boss):
    subordinates = [0 for i in range(n)]
    for i in range(1, n):
        subordinates[boss[i]-1] += 1
    return subordinates

if __name__ == '__main__':
    find_subordinates()