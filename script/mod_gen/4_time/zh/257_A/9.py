def problem257a(n, x):
    #print(n, x)
    i = 0
    while x > 0:
        i += 1
        x -= n
    print(chr(64 + i))

if __name__ == '__main__':
    problem257a()