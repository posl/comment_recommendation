def find_multiple_of_K(K):
    if K % 5 == 0:
        return -1
    
    x = 7 % K
    for i in range(1, K):
        if x == 0:
            return i
        x = (x * 10 + 7) % K
    return -1
