def count_layers(n):
    if n == 0:
        return 1
    return 2 * count_layers(n-1) + 3

if __name__ == '__main__':
    count_layers()