def get_length(n, k):
    if n == 0:
        return 1
    length = 0
    while n > 0:
        n = n // k
        length += 1
    return length

if __name__ == '__main__':
    get_length()