def S(n):
    n_str = str(n)
    sum = 0
    for i in n_str:
        sum += int(i)
    return sum

if __name__ == '__main__':
    S()