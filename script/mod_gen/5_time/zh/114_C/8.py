def check753(n):
    n_str = str(n)
    return (n_str.count('7') > 0 and n_str.count('5') > 0 and n_str.count('3') > 0)

if __name__ == '__main__':
    check753()