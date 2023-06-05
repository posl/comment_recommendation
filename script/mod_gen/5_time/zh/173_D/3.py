def get_max_comfort(n, list):
    # 1. get the max comfort for the first player
    comfort = 0
    for i in range(1, n):
        comfort += min(list[i-1], list[i])
    comfort += min(list[n-1], list[0])
    # 2. get the max comfort for the second player
    # 2.1 get the max comfort for the first player
    comfort2 = 0
    for i in range(2, n):
        comfort2 += min(list[i-1], list[i])
    comfort2 += min(list[n-1], list[1])
    comfort2 += min(list[0], list[1])
    # 2.2 get the max comfort for the second player
    comfort3 = 0
    for i in range(2, n):
        comfort3 += min(list[i-2], list[i])
    comfort3 += min(list[n-2], list[0])
    comfort3 += min(list[n-1], list[0])
    # 3. return the max comfort
    return max(comfort, comfort2, comfort3)

if __name__ == '__main__':
    get_max_comfort()