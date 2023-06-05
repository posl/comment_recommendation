def get_next_abc(n):
    while True:
        n += 1
        if n % 111 == 0:
            return n
