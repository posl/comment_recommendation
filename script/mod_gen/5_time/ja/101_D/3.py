def S(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

if __name__ == '__main__':
    S()