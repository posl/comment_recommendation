def get_binary_rep(n):
    binary_rep = []
    while n > 0:
        binary_rep.append(n % 2)
        n = n // 2
    return binary_rep

if __name__ == '__main__':
    get_binary_rep()