def get_binary(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n = n // 2
    return binary
