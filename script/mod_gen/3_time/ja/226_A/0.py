def my_round(x, d=0):
    p = 10 ** d
    return (x * p * 2 + 1) // 2 / p
x = input()
print(int(my_round(float(x), 0)))

if __name__ == '__main__':
    my_round()