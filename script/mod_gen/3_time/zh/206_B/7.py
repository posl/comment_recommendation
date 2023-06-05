def get_num(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
        if sum >= n:
            return i
    return 0

if __name__ == '__main__':
    get_num()