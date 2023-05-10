def get_path(n):
    path = []
    while n > 1:
        path.append(n)
        n //= 2
    return path

if __name__ == '__main__':
    get_path()