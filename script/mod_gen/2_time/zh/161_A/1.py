def exchange(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b

if __name__ == '__main__':
    exchange()