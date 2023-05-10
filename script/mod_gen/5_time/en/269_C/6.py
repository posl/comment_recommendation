def get_binary(x):
    binary = []
    while x > 0:
        binary.append(x % 2)
        x = x // 2
    return binary

if __name__ == '__main__':
    get_binary()