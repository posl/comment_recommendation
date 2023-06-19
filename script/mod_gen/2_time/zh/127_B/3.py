def get_result(r, D, x_2000):
    x_2001 = r * x_2000 - D
    print(x_2001)
    for i in range(2, 11):
        x_2001 = r * x_2001 - D
        print(x_2001)

if __name__ == '__main__':
    get_result()