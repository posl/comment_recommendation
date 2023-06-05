def get_min_num(n):
    min = n
    for i in range(1, n+1):
        temp = 0
        for j in range(n):
            temp += i**j
            if temp == n:
                return i
            elif temp > n:
                break
            else:
                continue
        if min > temp:
            min = temp
    return min

if __name__ == '__main__':
    get_min_num()