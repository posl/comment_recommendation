def get_name(n):
    if n <= 26:
        return chr(ord('a') + n - 1)
    else:
        return get_name((n-1) // 26) + get_name((n-1) % 26 + 1)

if __name__ == '__main__':
    get_name()