def get_num_of_stones(n, k, a):
    num_of_stones = 0
    for i in range(k-1, -1, -1):
        num_of_stones += (n//a[i])
        n = n%a[i]
    return num_of_stones
