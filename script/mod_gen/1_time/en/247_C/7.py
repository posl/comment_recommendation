def print_sequence(n):
    if n == 1:
        return [1]
    else:
        seq = print_sequence(n-1)
        return seq + [n] + seq

if __name__ == '__main__':
    print_sequence()