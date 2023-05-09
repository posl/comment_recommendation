def calc_joy(x):
    joy = 0
    while x >= 500:
        x -= 500
        joy += 1000
    while x >= 5:
        x -= 5
        joy += 5
    return joy

if __name__ == '__main__':
    calc_joy()