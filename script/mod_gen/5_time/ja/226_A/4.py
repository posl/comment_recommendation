def round_down(num, digit):
    p = 10 ** digit
    return (num * p // 1) / p
x = float(input())
print(round_down(x, 0))

if __name__ == '__main__':
    round_down()