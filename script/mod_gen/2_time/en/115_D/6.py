def num_layers(n):
    if n == 0:
        return 1
    return 2 + 2 * num_layers(n - 1)

if __name__ == '__main__':
    num_layers()