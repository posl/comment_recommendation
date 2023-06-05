def get_value(x, base):
    value = 0
    for i in range(len(x)):
        value = value * base + int(x[i])
    return value

if __name__ == '__main__':
    get_value()