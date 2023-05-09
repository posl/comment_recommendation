def sequence(n):
    if n == 1:
        return "1"
    else:
        return sequence(n-1) + " " + str(n) + " " + sequence(n-1)

if __name__ == '__main__':
    sequence()