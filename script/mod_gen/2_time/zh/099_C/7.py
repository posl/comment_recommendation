def get_min_operation(n):
    min_operation = n
    for i in range(0,n+1):
        for j in range(0,n+1):
            if 6**i + 9**j > n:
                break
            if 6**i + 9**j == n:
                min_operation = min(min_operation,i+j)
    return min_operation

if __name__ == '__main__':
    get_min_operation()