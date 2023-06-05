def cal_apple_pie(n,l):
    min_value = 1000000
    for i in range(n):
        temp = 0
        for j in range(n):
            if i != j:
                temp += l + j
        if abs(temp) < min_value:
            min_value = abs(temp)
    return min_value

if __name__ == '__main__':
    cal_apple_pie()