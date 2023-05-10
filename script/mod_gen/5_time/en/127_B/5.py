def calc_algae_growth(r, D, x_2000):
    x = x_2000
    for i in range(10):
        x = r * x - D
        print(x)

if __name__ == '__main__':
    calc_algae_growth()